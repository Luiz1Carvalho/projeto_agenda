from django import forms
from contact import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))
    
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

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if models.User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email existente', code='invalid'))
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email', 'username')   
    
    def save(self, commit = True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('As senhas diferentes', code='invalid'))

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email and models.User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email existente', code='invalid'))
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                for error in e.error_list:
                    self.add_error('password1', error)
        return password1