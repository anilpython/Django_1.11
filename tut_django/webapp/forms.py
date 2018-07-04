from django import forms
from .models import RestaurantLocation


class RestaurantLocationCreateFrom(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]

        def clean_name(self):
            title = self.cleaned_data.get("name")
            if title == "Hello":
                raise forms.ValidationError("You shoudn't type 'anil' as a name")
            return title
class RestaurantForm(forms.Form):
    owner = forms.CharField(max_length=100)
    location = forms.CharField(max_length=20)
    category = forms.CharField(max_length=10)


class A():
    pass
