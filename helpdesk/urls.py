from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('produtos/', include('produtos.urls')),
    path('servicos/', include('servicos.urls')),
    path('tecnicos/', include('tecnicos.urls')),
]