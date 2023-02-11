from django import forms

class Loginforms(forms.Form):
    username = forms.CharField(
        label=' Nome De Usuário: ',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Username'
            }
        )
    )
    senha = forms.CharField(
        label='Senha: ',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class" : "form-control",
                'placeholder': 'Password'
            }
        )
    )