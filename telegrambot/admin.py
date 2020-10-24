from django.contrib import admin
from .models import Accessbot

# Register your models here.


@admin.register(Accessbot)
class AccessbotAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name')
#
#
