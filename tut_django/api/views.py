from __future__ import unicode_literals
from rest_framework import generics
from webapp.models import RestaurantLocation
from .serializers import RestaurantCreateSerializers,RestaurantSerializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class RestaurantsCreate(generics.CreateAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantCreateSerializers
    permission_classes = [IsOwnerOrReadOnly]#IsAdminUser

    # def perform_create(self,serializer):
    #     serializer.save(owner = self.request.owner)

class RestaurantsList(generics.ListAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantSerializers
    pagination_class = LimitOffsetPagination #PageNumberPagination

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantSerializers
    lookup_field = "slug"
    #pagination_class = LimitOffsetPagination #PageNumberPagination

class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantSerializers
    lookup_field = "slug"

    # def perform_update(self,serializer):
    #     serializer.save(owner = self.request.owner)

class RestaurantDeleteView(generics.DestroyAPIView):
    queryset = RestaurantLocation.objects.all()
    serializer_class = RestaurantSerializers
    lookup_field = "slug"
