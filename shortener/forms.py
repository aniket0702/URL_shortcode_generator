from django import forms
from django.core.validators import URLValidator
class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = 'Submit Url')

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
            value_1_invalid = True
        value_2_url = "http://"+url
        try:
            url_validator(url)
        except:
            value_2_invalid = True

        if not ".com" in url and not value_1_invalid and not value_2_invalid:
            raise forms.ValidationError("No .com")
        return cleaned_data

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL ")
        # return url
