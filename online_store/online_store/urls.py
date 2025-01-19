"""
URL configuration for megano project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import (
    AboutView,
    CatalogViewSet,
    ProductViewSet,
    OrderViewSet,
    OrderDetailView,
    ProfileView,
    SignInView,
    SignUpView,
)

router = DefaultRouter()
router.register(r'catalog', CatalogViewSet)
router.register(r'product', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about'),
    path('catalog/<int:id>/', ProductViewSet.as_view({'get': 'retrieve'}), name='catalog-detail'),
    path('orders/order-detail/', OrderDetailView.as_view(), name='order-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('', include(router.urls)),
]
