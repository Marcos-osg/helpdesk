from django.urls import path
from produtos import views


urlpatterns = [
    path('', views.produto, name='product'),
    path('novo_produto', views.new_product, name='new-product'),
]