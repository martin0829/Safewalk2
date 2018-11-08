from django.shortcuts import render
from django.http import JsonResponse
from .models import Walker, Party, Region
from .serializers import WalkerSerializer, PartySerializer, RegionSerializer
from rest_framework import viewsets

class WalkerViewSet(viewsets.ModelViewSet):
    queryset = Walker.objects.all()
    serializer_class = WalkerSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer