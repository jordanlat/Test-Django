from django import forms

class NameForm(forms.Form):
    nom    = forms.CharField(label='Nom', max_length=20)
    prenom = forms.CharField(label='Prénom', max_length=30)