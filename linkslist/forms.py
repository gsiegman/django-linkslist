from django import forms
from django.conf import settings
from linkslist.models import LinksListItem, LinksListItemImage

class LinksListItemAdminForm(forms.ModelForm):
    class Meta:
        model = LinksListItem
