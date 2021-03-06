from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
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


class QuoteUpdateViewSet(UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class QuoteDeleteViewSet(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def perform_destroy(self, instance):
        return instance.delete()


class QuoteRatingAddViewSet(UpdateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def perform_update(self, serializer):

        if not f"rating_add_{serializer.instance.pk}" in self.request.session:
            self.request.session[f"rating_add_{serializer.instance.pk}"] = False

        if self.request.session[f"rating_add_{serializer.instance.pk}"] == False:
            serializer.instance.rating += 1
            serializer.instance.save()
            self.request.session[f"rating_add_{serializer.instance.pk}"] = True
            self.request.session[f"rating_remove_{serializer.instance.pk}"] = False

        return serializer


class QuoteRatingRemoveViewSet(UpdateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def perform_update(self, serializer):

        if not f"rating_remove_{serializer.instance.pk}" in self.request.session:
            self.request.session[f"rating_remove_{serializer.instance.pk}"] = False

        if self.request.session[f"rating_remove_{serializer.instance.pk}"] == False:
            if not serializer.instance.rating == 0:
                serializer.instance.rating -= 1
                serializer.instance.save()
                self.request.session[f"rating_remove_{serializer.instance.pk}"] = True
                self.request.session[f"rating_add_{serializer.instance.pk}"] = False

        return serializer