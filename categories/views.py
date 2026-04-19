from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminUserOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework import status


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        category = self.get_object()
        products = category.products.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_categories = Category.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_categories, many=True)
        return Response(serializer.data)
    
    # Check if the category has products before allowing deletion
    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        if category.products.exists():
            return Response({'error': 'There are products connected to this category that mean it can\'t be deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(category)
        return Response(
        {"success": 'true',
        'message': 'Category deleted successfully.'},
        status=status.HTTP_200_OK
    )