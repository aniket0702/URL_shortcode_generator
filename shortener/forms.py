from django import forms
from django.core.validators import URLValidator
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = '',widget = forms.TextInput(attrs = {"placeholder":"Long URL"}))

    def clean(self):
        cleaned_data = super(SubmitUrlForm,self).clean()
        value_1_invalid = False
        value_2_invalid = False
        url = cleaned_data.get('url')
        print("maiofmoaid")
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Give the correct url")
        print (".com" in url)
        if (".com" in url) == False:
            raise forms.ValidationError("No .com")
        return cleaned_data
