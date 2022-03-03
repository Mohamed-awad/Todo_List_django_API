from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdminModel(admin.ModelAdmin):
    """Admin model for customizing task model admin view"""

    list_display = [
        'id', 'title', 'end_user', 'status', 'due_date'
    ]

    search_fields = ['id', 'title']
    readonly_fields = ['id']
    ordering = ['-id']
