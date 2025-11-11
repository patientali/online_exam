from django.db import models
from accounts.models import User
from grading.models import Submission

class Notification(models.Model):
    TYPE_CHOICES = (
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('both', 'Both'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='email')
    sent_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user}: {self.message[:50]}..."