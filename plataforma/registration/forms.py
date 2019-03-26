from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required 254 characters maximum and must be valid")
    widgets = {
        'username': forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Username'}),
        'email': forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'}),
        'password1': forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Password'}),
        'password2': forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Re password'}),
    }
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email is already registered, try another.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Bio'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Link'}),
        }
        labels = {
            'avatar': '',
            'bio': '',
            'link': '',
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Required 254 characters maximum and must be valid")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("The email is already registered, try another.")
        return email
