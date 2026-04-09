
from django import forms
from contact import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)

        #widgets = {'first_name': forms.PasswordInput()}

        widgets = {'first_name': forms.TextInput(
            attrs={'class': 'form-control', 
                   'placeholder': 'Seu nome'})}
