from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    model = User  # Specify the custom user model
    
    list_display = ('username', 'email','role','is_staff')

    # Display fields when editing an existing user record
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {
            'fields':('role',),
        }),
    )

    # Display fields when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {
            'fields': ('role',),
        }),
    )



# Register your CustomUser model with your CustomUserAdmin layout
# admin.site.register(User, CustomUserAdmin)
