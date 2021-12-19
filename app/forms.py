from django import forms
from .models import Post

class PeopleRegistration(forms.ModelForm):
    class Meta:
        model=Post
        fields= ['name', 'email', 'password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True)
        }