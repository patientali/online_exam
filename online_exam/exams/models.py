from django.db import models
from accounts.models import User

class Exam(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'professor'})
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    duration = models.DurationField() 
    total_score = models.FloatField(default=100.0)
    topic = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class Question(models.Model):
    TYPE_CHOICES = (
        ('short_answer', 'Short Answer'),
        ('multiple_choice', 'Multiple Choice'),
        ('file_upload', 'File Upload'),
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    correct_answer = models.TextField(blank=True, null=True) 
    options = models.JSONField(blank=True, null=True)  
    score = models.FloatField(default=1.0)  

    def __str__(self):
        return f"{self.text[:50]}..."  