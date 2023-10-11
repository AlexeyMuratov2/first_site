from django.forms import ModelForm, TextInput, Textarea
from .models import SiteRequest

class SiteForm(ModelForm):
    class Meta:
        model = SiteRequest
        fields = ('site_name', 'description', 'urgently', 'customer')