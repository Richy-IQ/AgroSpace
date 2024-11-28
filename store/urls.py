from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from .views import (ProductViewSet, CollectionViewSet, CartViewSet, CustomerViewSet, PromotionViewSet, ProductImageViewSet,
                    OrderItemViewSet, OrderViewSet, CommentViewSet, AddressViewSet, ReviewViewSet, CartItemViewSet,
                    RegisterView, LoginView, LogoutView,  InitializePaymentView, VerifyPaymentView,)

router = routers.DefaultRouter()
router = DefaultRouter()
router.register(r'promotions', PromotionViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('paystack/initialize/', InitializePaymentView.as_view(), name='initialize-payment'),
    path('paystack/verify/<str:reference>/', VerifyPaymentView.as_view(), name='verify-payment')
]
