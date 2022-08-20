from django import forms
from django.forms import fields
from .models import MembershipEmail, Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'
        
class MembershipEmailForm(forms.ModelForm):
    class Meta:
        model = MembershipEmail
        fields = '__all__'