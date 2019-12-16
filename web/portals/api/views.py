from rest_framework.views import APIView
from rest_framework.response import Response

from portals.models import Portal
from .serializers import PortalSerializer


class PortalList(APIView):
    def get(self, _):
        portals = Portal.objects.all()
        serializer = PortalSerializer(portals, many=True)
        return Response(serializer.data)


class PortalDetailView(APIView):
    def get(self, _, _id):
        portal = Portal.objects.get(id=_id)
        portal_weblet = portal.portal_weblet.all()
        weblets = [{
            'title': pw.weblet.title,
            'img_url': pw.weblet.picture_thumbnail.url,
            'created_by': pw.weblet.created_by.email,
            'created_on': pw.weblet.created_on
        } for pw in portal_weblet]
        return Response({
            'weblets': weblets
        })

