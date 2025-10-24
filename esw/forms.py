from django import forms
from .models import ContactMessage
from .models import (
    candidateDetails,
    ftherDetails,
    mtherDetails,
    GuardDetails,
    emergencyContact1,
    emergencyContact2,
    emergencyContact3,
    schUpdate,
)


class CandidateForm(forms.ModelForm):
    class Meta:
        model = candidateDetails
        fields ='__all__'

class FatherForm(forms.ModelForm):
    class Meta:
        model = ftherDetails
        fields = '__all__'

class MotherForm(forms.ModelForm):
    class Meta:
        model = mtherDetails
        fields = '__all__'

class GuardianForm(forms.ModelForm):
    class Meta:
        model = GuardDetails
        fields = '__all__'

class Emergency1Form(forms.ModelForm):
    class Meta:
        model = emergencyContact1
        fields = '__all__'

class Emergency2Form(forms.ModelForm):
    class Meta:
        model = emergencyContact2
        fields = '__all__'

class Emergency3Form(forms.ModelForm):
    class Meta:
        model = emergencyContact3
        fields = '__all__'

class SchUpdateForm(forms.ModelForm):
    class Meta:
        model = schUpdate
        fields = '__all__'







class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Type your message here...'
            }),
        }
