from django.urls import path

from api_v1.views import QuoteListCreateViewSet, QuoteView, QuoteCreateView

urlpatterns = [
    path("quote/", QuoteListCreateViewSet.as_view(), name="quote"),
    path("quote/<int:pk>/", QuoteView.as_view(), name="quote_detail"),
    path("quote/create/", QuoteCreateView.as_view(), name="quote_create")

]