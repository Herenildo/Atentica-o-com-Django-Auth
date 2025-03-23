from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth import authenticate

class UsuarioCPFForm(UserCreationForm):
    cpf = forms.CharField(label='CPF', max_length=14)
    first_name = forms.CharField(label='Nome completo', max_length=150)
    email = forms.EmailField(label='E-mail')
    username = forms.CharField(label='Nome de usuário', max_length=150)

    class Meta:
        model = Usuario
        fields = ['first_name', 'cpf', 'email', 'username', 'password1', 'password2']

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Este CPF já está cadastrado.")
        return cpf

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username


class LoginCPFForm(forms.Form):
    cpf = forms.CharField(label='CPF')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        password = cleaned_data.get('password')

        try:
            user = Usuario.objects.get(cpf=cpf)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("CPF não encontrado.")

        user = authenticate(username=user.username, password=password)

        if user is None:
            raise forms.ValidationError("CPF ou senha incorretos.")

        self.user = user
        return cleaned_data
