from django.forms import ModelForm
from  .models import*

class Editor(ModelForm):
    class Meta:
        model=Editor
        fields=['title','body']