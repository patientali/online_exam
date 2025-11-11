from django.db import models
from accounts.models import User
from exams.models import Exam, Question

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='submissions')
    start_time = models.DateTimeField(auto_now_add=True) 
    submitted_at = models.DateTimeField(null=True, blank=True)
    total_score = models.FloatField(null=True, blank=True) 

    def __str__(self):
        return f"Submission by {self.student} for {self.exam}"

class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    answer_file = models.FileField(upload_to='answers/', blank=True, null=True) 
    graded_score = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"Answer for {self.question} in {self.submission}"