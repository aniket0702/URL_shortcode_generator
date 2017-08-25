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

        if ".com" in url == False:
            raise forms.ValidationError("No .com")
        value_2_url = "http://"+url
        try:
            url_validator(value_2_url)
        except:
            value_2_invalid = True

        if not value_1_invalid and not value_2_invalid:
            raise forms.ValidationError("No http")
        return cleaned_data

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL ")
        # return url
