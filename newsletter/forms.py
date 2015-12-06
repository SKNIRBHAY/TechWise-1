from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, max_length=400)

class SignUpUser(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['username','email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
       # email_base, provider = email.split("@")
        return email

    def clean_last_name(self):
        full_name = self.cleaned_data.get('last_name')
        return full_name


