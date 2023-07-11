from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# Creating Router object
router = DefaultRouter()

router.register('blogging', BlogPostModelViewSet, basename='blogpost')

urlpatterns = [
    path('api/', include(router.urls)),
]
