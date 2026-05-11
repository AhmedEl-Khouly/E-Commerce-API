from .models import Cart, CartItem
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    sub_total = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'product_price', 'quantity', 'sub_total']
    
    def total(self, obj):
        return obj.product.price * obj.quantity

class AddToCartSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        cart_item, created = CartItem.objects.get_or_create(cart_id=cart_id, product_id=product_id)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        
        return cart_item 

    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'updated_at', 'total_price', 'items']
