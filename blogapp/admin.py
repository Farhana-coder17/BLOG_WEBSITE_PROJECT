# Register your models here.
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Show these fields in admin panel
    search_fields = ('title', 'content', 'user__username')  # Search by title or username
    list_filter = ('created_at',)  # Add a filter by date
