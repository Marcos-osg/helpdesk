from django.urls import path
from tecnicos import views


urlpatterns = [
    path('',views.tecnico, name='technician'),
    path('novo_tecnico',views.new_technician, name='new-technician'),
    path('detalhes/<int:id_tecnico>', views.detail_technician, name='technician-details'),
]