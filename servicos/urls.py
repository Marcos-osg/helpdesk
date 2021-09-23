from django.urls import path
from servicos import views


urlpatterns = [
    path('',views.service, name='services' ),
    path('novo_servico',views.new_service, name='new-service'),
    path('detalhe/?P<id>[0-9]+',views.detail_service, name='detail-service'),
    path('deletar/?P<id>[0-9]+', views.delete_service, name='service-delete'),
    path('editar/?P<id>[0-9]+', views.edita_service, name='service-edit'),
]