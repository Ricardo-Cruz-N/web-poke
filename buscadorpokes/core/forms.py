from django import forms

class SubmitPoke(forms.Form):
    url = forms.URLField()