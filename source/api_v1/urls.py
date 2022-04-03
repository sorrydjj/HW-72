from django.urls import path

from api_v1.views import QuoteListCreateViewSet

urlpatterns = [
    path("quote/", QuoteListCreateViewSet.as_view(), name="quote")
]