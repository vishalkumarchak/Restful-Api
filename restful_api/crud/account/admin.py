from django.contrib import admin
from .models import User, Item
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModalAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "tc", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []

    
# Now register the new UserAdmin...
admin.site.register(User, UserModalAdmin)

@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

