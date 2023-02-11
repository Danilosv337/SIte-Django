from django import forms

class New_projectforms(forms.Form):
    project_name = forms.CharField(
        label='Nome Do Projeto',
        max_length=200
    )
    project_img = forms.ImageField(
        label="Imagem Do Projeto",
        required=False,
    )
    project_legend = forms.CharField(
        label='Legenda'
    )
    project_descricao = forms.CharField(
        label='Descricao',
        widget=forms.Textarea
    )
    project_link = forms.CharField(

    )