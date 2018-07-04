from django.conf.urls import url
from . import views
#app_name = "webapp"


urlpatterns = [
    url(r'^$',views.ItemListView.as_view(),name="list_view"),
    url(r'create/create/',views.ItemCreateView.as_view(),name="create_view"),
    url(r'^(?P<pk>[\d-]+)/$',views.ItemDetailView.as_view(),name="detail_view"),
]