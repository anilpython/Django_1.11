from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

app_name = "webapp"


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<slug>[\w-]+)/$',views.RestaurantListView.as_view(),name="Restaurant_Lists"),
    #url(r'^(?P<slug>[\w-]+)/$', views.RestaurantDetailView.as_view(), name="Restaurant_Details"),
    url(r'Home/',views.home,name="home"),
    url(r'About/',views.AboutView.as_view(),name="about"),
    url(r'Contact/',views.ContactView.as_view(),name="contact"),
    url(r'create/create/',views.RestaurantCreateView.as_view(),name="create_view"),
    #url(r'login/login/$',LoginView.as_View()),
]