from django.contrib import admin
from .models import userModel
# Register your models here.
@admin.register(userModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('id','Full_Name','Email','Address','Phone_Number','Birth_Date')
