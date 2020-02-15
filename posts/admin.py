from django.contrib import admin
from django.contrib.auth.models import User
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'photo',
        'user',
        'created',
        'modified',
    )

    list_display_links = (
        'title',
    )

    list_filter = (
        'created',
        'modified',
    )

    fieldsets = (
        ('User', {
            'fields': (('user', 'profile'),),
        }),
        ('Content', {
            'fields': (
                ('title'),
                ('photo'),
            ),
        }),
    )

