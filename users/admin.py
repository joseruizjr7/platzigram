# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture',
    )

    list_display_links = (
        'pk',
        'user',
        'phone_number',
    )

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
        )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified',)

# This allows you to add a new profile at the same time that the user and shows it in the same screen.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
##