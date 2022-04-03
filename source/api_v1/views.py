from rest_framework.generics import ListCreateAPIView

from api_v1.serializers import QuoteSerializer
from rest_framework.permissions import AllowAny

from webapp.models import Quote


class QuoteListCreateViewSet(ListCreateAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Quote.objects.all()
        else:
            return Quote.objects.filter(status="moderated")