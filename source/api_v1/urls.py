from django.urls import path

from api_v1.views import QuoteListCreateViewSet, QuoteView

urlpatterns = [
    path("quote/", QuoteListCreateViewSet.as_view(), name="quote"),
    path("quote/<int:pk>/", QuoteView.as_view(), name="quote_detail")
]