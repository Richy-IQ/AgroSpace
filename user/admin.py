from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User



class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("username", "password1", "password2", "email", "first_name", "last_name")
                },
            ),
        )

admin.site.register(User, UserAdmin)

