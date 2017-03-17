from django.contrib import admin
from .models import Custom_User
# Register your models here.

class Custom_User_Amdin(admin.ModelAdmin):
    class Meta:
        model = Custom_User

admin.site.register(Custom_User, Custom_User_Amdin)
