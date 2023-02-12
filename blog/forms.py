from django import forms
from blog.models import Projetos

class New_projectforms(forms.ModelForm):
    class Meta:
        model = Projetos
        exclude = ()
    