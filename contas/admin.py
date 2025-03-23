from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'cpf', 'email', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
                ('Dados pessoais', {'fields': ('cpf',)}),
)
