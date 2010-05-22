from django import forms
from django.conf import settings
from linkslist.models import LinksListItem, LinksListItemImage
from ajax_filtered_fields.forms import ForeignKeyByLetter

class LinksListItemAdminForm(forms.ModelForm):
    image = ForeignKeyByLetter(LinksListItemImage, field_name="name", required=False)
    
    class Meta:
        model = LinksListItem

    class Media:
        js = (settings.ADMIN_MEDIA_PREFIX + "js/SelectBox.js",
                 settings.ADMIN_MEDIA_PREFIX + "js/SelectFilter2.js",
                 "http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js",
                 settings.STATIC_URL + "js/ajax_filtered_fields.js",)
