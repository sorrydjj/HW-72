from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView

from api_v1.serializers import QuoteSerializer

from webapp.models import Quote


class QuoteListCreateViewSet(ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Quote.objects.all()
        else:
            return Quote.objects.filter(status="moderated")

class QuoteView(RetrieveAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Quote.objects.all()
        return Quote.objects.filter(status="moderated")


class QuoteCreateView(CreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
