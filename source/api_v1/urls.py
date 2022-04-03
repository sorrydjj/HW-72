from django.urls import path

from api_v1.views import QuoteListCreateViewSet, QuoteView, QuoteCreateView, QuoteUpdateViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token, name='api_token_auth'),
    path("quote/", QuoteListCreateViewSet.as_view(), name="quote"),
    path("quote/<int:pk>/", QuoteView.as_view(), name="quote_detail"),
    path("quote/create/", QuoteCreateView.as_view(), name="quote_create"),
    path("quote/<int:pk>/update/", QuoteUpdateViewSet.as_view(), name="quote_update")

]