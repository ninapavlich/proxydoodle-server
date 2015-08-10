from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.html import escape, format_html, format_html_join, smart_urlquote
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from imagekit_cropper.widgets import ImageCropWidget    

from .models import *



    

class ImageAdminForm(forms.ModelForm):
    square_crop = forms.CharField(widget=ImageCropWidget(properties=Image.square_crop_properties, help_text=Image.help['square_crop']))


    width_1200_wide_crop = forms.CharField(widget=ImageCropWidget(properties=Image.width_1200_wide_crop_properties, help_text=Image.help['width_1200_wide_crop']))
    
    class Meta:
        model = Image
        fields = '__all__'


	def __init__(self, *args, **kwargs):
		super(ImageAdminForm, self).__init__(*args, **kwargs)

		#TODO -- move to cropper
		self.fields['image'].help_text = _("Be sure to (color profile message TODO...). Files over 10MB will have trouble being cropped.")