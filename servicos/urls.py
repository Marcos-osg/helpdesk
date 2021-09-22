from django.urls import path
from servicos import views


urlpatterns = [
    path('',views.service, name='services' ),
    path('novo_servico',views.new_service, name='new-service'),
    path('detalhe/?P<id>[0-9]+',views.detail_service, name='detail-service'),
]