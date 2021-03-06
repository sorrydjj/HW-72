from django.urls import path

from api_v1.views import (QuoteListCreateViewSet,
                          QuoteView,
                          QuoteCreateView,
                          QuoteUpdateViewSet,
                          QuoteDeleteViewSet,
                          QuoteRatingAddViewSet,
                          QuoteRatingRemoveViewSet)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token, name='api_token_auth'),
    path("quote/", QuoteListCreateViewSet.as_view(), name="quote"),
    path("quote/<int:pk>/", QuoteView.as_view(), name="quote_detail"),
    path("quote/create/", QuoteCreateView.as_view(), name="quote_create"),
    path("quote/<int:pk>/update/", QuoteUpdateViewSet.as_view(), name="quote_update"),
    path("quote/<int:pk>/delete/", QuoteDeleteViewSet.as_view(), name="quote_delete"),
    path("quote/<int:pk>/rating/add/", QuoteRatingAddViewSet.as_view(), name="quote_rating_add"),
    path("quote/<int:pk>/rating/remove/", QuoteRatingRemoveViewSet.as_view(), name="quote_rating_remove")

]