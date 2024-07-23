from rest_framework import routers
from .api import Projectviewset
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('api/projects', Projectviewset, 'projects')

urlpatterns = router.urls 