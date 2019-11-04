from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from tags.models import Tag
from .serializers import TagSerializer


class TagList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, _):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
