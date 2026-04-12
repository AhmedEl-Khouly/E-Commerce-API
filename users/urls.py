from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserProfileViewSet, RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register("profile", UserProfileViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("",include(router.urls)),
    path("register/", RegisterView.as_view()),
    path("profile/update/", RetrieveUpdateAPIView.as_view()),
    path('auth/', include('djoser.urls')),
]
