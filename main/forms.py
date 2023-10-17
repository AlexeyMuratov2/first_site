from django.forms import ModelForm, TextInput, Textarea
from .models import SiteOrder
from django.forms.widgets import HiddenInput


class SiteForm(ModelForm):
    class Meta:
        model = SiteOrder
        fields = ('site_name', 'description', 'urgently', 'user',)
        widgets = {'user': HiddenInput()}