from django.contrib import admin
from django.contrib import admin
from accounts.models import User

# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    list_display = '__all__'
    
admin.site.register(User)