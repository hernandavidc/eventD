from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name','city','description','private','date','drctn','image','cost','urlMaps','urlPay']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'private': forms.CheckboxInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'drctn': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'cost': forms.NumberInput(attrs={'class':'form-control'}),
            'city': forms.Select(attrs={'class':'form-control'}),
            'urlMaps': forms.URLInput(attrs={'class':'form-control'}),
            'urlPay': forms.URLInput(attrs={'class':'form-control'}),
        }