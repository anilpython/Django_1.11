from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField , SerializerMethodField
from webapp.models import RestaurantLocation

class RestaurantSerializers(ModelSerializer):
    slug_url = HyperlinkedIdentityField(
        view_name = 'api:detail',
        lookup_field = 'slug',
        )
    owner = SerializerMethodField()
    class Meta:
        model = RestaurantLocation
        fields = [
            'slug_url',
            'owner',
            'name',
            'location',
            'category',
            'timestamp',
            'updated',
            'slug',
        ]
    def get_owner(self, obj):
        return str(obj.owner.username)
class RestaurantCreateSerializers(ModelSerializer):
    class Meta:
        model = RestaurantLocation
        fields = [
            'owner',
            'name',
            'location',
            'category',
        ]