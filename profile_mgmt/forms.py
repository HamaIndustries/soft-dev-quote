from django import forms
import re

text_re = re.compile("[0-9]")

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=9, min_length=5)

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if text_re.match(name):
            raise forms.ValidationError("Enter a valid value.")
        return name