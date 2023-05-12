from django import forms


class ShortForm(forms.Form):
    url = forms.URLField(label="URL", max_length=255)
