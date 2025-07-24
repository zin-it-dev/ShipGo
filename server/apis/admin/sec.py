from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ["email", "username", "is_active"]
    prepopulated_fields = {"slug": ("last_name", "first_name")}
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        ("Personal info", {"fields": ["slug", "first_name", "last_name", "avatar"]}),
        ("Permissions", {"fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password", "confirm_password", "slug", "first_name", "last_name", "avatar", "is_active", "is_staff", "is_superuser"],
            },
        ),
    ]
    search_fields = ["email", "username", "first_name", "last_name"]
    ordering = ["email"]
    filter_horizontal = []