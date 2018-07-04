from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import RestaurantLocation
from django.views.generic.base import View,TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.db.models import Q
from .forms import RestaurantLocationCreateFrom
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RestaurantForm
from django.forms import formset_factory


def index(request):
    queryset = RestaurantLocation.objects.all()
    ArticleFormSet = formset_factory(RestaurantForm, extra=2)
    formset = ArticleFormSet()
    return render(request,"index.html",{'page_name':"index",'Restaurant_lists':queryset,'formset':formset })

class RestaurantListView(DetailView):
    template_name = "restaurant_location.html"
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset =  RestaurantLocation.objects.filter(Q(slug__iexact=slug) |
                                                          Q(slug__icontains=slug))
            return queryset
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


def home(request):
    return render(request,"home.html",{'page_name':"home"})

class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self,*args,**kwargs):
        context = super(AboutView,self).get_context_data(*args,**kwargs)
        dict = {"page_name":"About"}
        return dict

class ContactView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        page_name = {"page_name":"Contact"}
        return render(request,"contact.html",page_name)

class RestaurantCreateView(LoginRequiredMixin ,CreateView):
    form_class = RestaurantLocationCreateFrom
    template_name = 'form.html'
    success_url = "/webapp/"

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self,*args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add a Restaurant'
        return context