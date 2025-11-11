from django.contrib import admin
from .models import Exam, Question

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'professor', 'start_time', 'duration', 'total_score', 'topic')
    list_filter = ('topic', 'start_time')
    search_fields = ('title', 'topic')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question_type', 'text_preview', 'score')
    list_filter = ('question_type', 'exam')
    search_fields = ('text',)

    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Question'