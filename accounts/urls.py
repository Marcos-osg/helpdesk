from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # urls de login e cadastro de usuario
    path('',views.login, name='login'),
    path('login-sucess',views.login_sucess, name='login-sucess'),
    path('cadastro', views.cadastrar, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),
        name='reset_password'),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_sent.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
        name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'), 
        name='password_reset_complete'),
    
    # urls de clientes e cadastro de clientes
    path('clientes',views.clientes, name='client-list'),
    path('new_client',views.novo_cliente, name='new-client'),
    path('detalhe/?P<id>[0-9]+',views.detalhe_cliente, name='detail-client'),
    path('excluir/?P<id>[0-9]+',views.excluir_cliente, name='delete-client'),
]