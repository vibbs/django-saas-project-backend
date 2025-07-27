from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .. import views

router = DefaultRouter()
router.register(r'users', views.AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
]