from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from main.views import WalkerViewSet, PartyViewSet, RegionViewSet

router = DefaultRouter()
router.register(r'walkers', WalkerViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = router.urls