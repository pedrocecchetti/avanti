from .custom_admin.contact import ContactAdmin
from .custom_admin.user import CustomUserAdmin
from django.contrib import admin
from .models import User, Contact

# Register your models here.

admin.site.register(User, CustomUserAdmin)
admin.site.register(Contact, ContactAdmin)
