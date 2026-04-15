from django import forms
from contact import models
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*'}))
    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')

        #widgets = {'first_name': forms.PasswordInput()}

        widgets = {'first_name': forms.TextInput(
            attrs={'class': 'form-control', 
                   'placeholder': 'Seu nome'})}
        
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        msg = ValidationError('O nome e sobrenome não podem ser iguais', code='invalid')
        if first_name ==  last_name:
            self.add_error('last_name', msg)
        

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == "ASD":
            self.add_error('first_name', ValidationError('Não pode ser esse nome', code='invalid'))
        return first_name
