from django.urls import path
from tecnicos import views


urlpatterns = [
    path('',views.tecnico, name='technician'),
    path('novo_tecnico',views.new_technician, name='new-technician'),
    path('detalhes/?P<id>[0-9]+', views.detail_technician, name='technician-details'),
    path('deletar/?P<id>[0-9]+', views.delete_technician, name='technician-delete'),
    path('editar/?P<id>[0-9]+', views.edita_tecnico, name='technician-edit'),
]