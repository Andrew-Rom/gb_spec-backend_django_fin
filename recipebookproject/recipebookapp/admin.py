from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from recipebookapp.models import CustomUser


@admin.register(CustomUser)
class ClientAdmin(BaseUserAdmin):
    pass
