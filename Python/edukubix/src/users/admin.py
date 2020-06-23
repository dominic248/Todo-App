from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *



class UserAdmin(admin.ModelAdmin):  
    form = UserAdminForm
    
admin.site.register(User)
# admin.site.register(User, UserAdmin)
 