from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='contas/login_username.html'), name='login'),
    path('login-cpf/', views.login_cpf, name='login_cpf'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastrar_usuario_comum, name='cadastro_usuario'),
    path('painel/', views.painel, name='painel'),
    path('senha/reset/', auth_views.PasswordResetView.as_view(
        template_name='contas/password_reset.html'), name='password_reset'),
        
    path('senha/reset/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='contas/password_reset_done.html'), name='password_reset_done'),

    path('senha/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='contas/password_reset_confirm.html'), name='password_reset_confirm'),

    path('senha/reset/feito/', auth_views.PasswordResetCompleteView.as_view(
        template_name='contas/password_reset_complete.html'), name='password_reset_complete'),
]
