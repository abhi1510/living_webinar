import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from weblets.models import Weblet
from presenters.models import Presenter


@api_view(['POST'])
def manipulate_weblet_presenter(request):
    weblet_id = request.POST.get('weblet_id')
    weblet = Weblet.objects.get(id=weblet_id)
    presenters = json.loads(request.POST.get('presenters'))
    for _id, status in presenters.items():
        presenter = Presenter.objects.get(id=_id)
        if status:
            weblet.presenters.add(presenter)
        else:
            weblet.presenters.remove(presenter)
    return Response({})
