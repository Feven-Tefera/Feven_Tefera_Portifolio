from django.contrib import admin

# Register your models here.
# admin.py
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'message')
    search_fields = ('first_name', 'last_name', 'email')
