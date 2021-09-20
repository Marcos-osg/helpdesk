from django.urls import path
from produtos import views


urlpatterns = [
    path('', views.produto, name='product'),
    path('detalhe/<int:id_produto>', views.produto_detalhe, name='product-details'),
    path('novo_produto', views.new_product, name='new-product'),
]