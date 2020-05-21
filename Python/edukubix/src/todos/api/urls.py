from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router=DefaultRouter()
router.register('todo',TodoViewSet)



urlpatterns = [
    path('', include(router.urls)),
]