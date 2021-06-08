from django.forms import ModelForm
from .models import Image

class GalleryForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"
    
   