from rest_framework import serializers
from .models import Walker, Party, Region

class WalkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Walker
        fields = ('username', 'email', 'photo', 'rating', 'emgContact', 'party')

class PartySerializer(serializers.ModelSerializer):
    walkers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Party
        field = ('startLoc', 'endLoc', 'departTime', 'walkers')

class RegionSerializer(serializers.ModelSerializer):
    parties = serializers.StringRelatedField(many=True)
    class Meta:
        model = Region
        field = ('name', 'description', 'long', 'lat', 'parties')