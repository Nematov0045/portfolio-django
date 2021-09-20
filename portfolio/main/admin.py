from django.contrib import admin
from django.db import models
from .models import SendMessage

# Register your models here.
class SendMessageAdmin(admin.ModelAdmin):
    list_display=("pk","email","phone_number","message","send_at")
    search_fields=("email",)
    list_editable=("message",)
    list_filter=("send_at",)
    ordering=("send_at",)
admin.site.register(SendMessage,SendMessageAdmin)
