from django.urls import path
from produtos import views


urlpatterns = [
    path('', views.produto, name='product'),
    path('detalhe/?P<id>[0-9]+', views.produto_detalhe, name='product-details'),
    path('novo_produto', views.new_product, name='new-product'),
    path('deletar_produto/?P<id>[0-9]+',views.deletar_produto, name='deletar-produto'),
]