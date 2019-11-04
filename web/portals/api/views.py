from rest_framework.views import APIView
from rest_framework.response import Response

from portals.models import Portal
from .serializers import PortalSerializer


class PortalList(APIView):
    def get(self, _):
        portals = Portal.objects.all()
        serializer = PortalSerializer(portals, many=True)
        return Response(serializer.data)
