from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'submission', 'notification_type', 'sent_at', 'is_sent', 'is_read')
    list_filter = ('notification_type', 'is_sent', 'is_read')
    readonly_fields = ('sent_at',)