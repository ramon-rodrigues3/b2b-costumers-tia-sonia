from django.urls import path, include
from api.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()

router.register('vendedor', VendedorViewSet)
router.register('cliente', ClienteViewSet)
router.register('configuracao', ConfiguracaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth-token/', views.obtain_auth_token)
]