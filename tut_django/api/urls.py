from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',RestaurantsList.as_view(),name="list"),
    url(r'^(?P<slug>[\w-]+)/$',RestaurantDetailView.as_view(),name="detail"),
    url(r'^(?P<slug>[\w-]+)/edit/$',RestaurantUpdateView.as_view(),name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$',RestaurantDeleteView.as_view(),name="delete"),
    url(r'create/create/$',RestaurantsCreate.as_view(),name="create"),
]