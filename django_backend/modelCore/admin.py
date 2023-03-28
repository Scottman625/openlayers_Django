from django.contrib import admin
from .models import User,Drawdata

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')

@admin.register(Drawdata)
class DrawdataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'jsondata', )