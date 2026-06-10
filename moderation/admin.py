from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ModerationResult

@admin.register(ModerationResult)
class ModerationResultAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'category',
        'risk_level',
        'allowed',
        'report_generated',
        'created_at'
    )

    list_filter = (
        'category',
        'risk_level',
        'allowed',
        'report_generated'
    )

    search_fields = (
        'text',
        'category'
    )