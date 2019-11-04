from rest_framework import serializers

from portals.models import Portal, PortalWeblet


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = '__all__'


class PortalWebletSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalWeblet
        fields = '__all__'
