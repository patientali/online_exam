from django.contrib import admin
from .models import Submission, Answer

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'start_time', 'submitted_at', 'total_score')
    list_filter = ('exam',)
    readonly_fields = ('start_time', 'submitted_at')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'question', 'answer_preview', 'graded_score')
    list_filter = ('question__question_type',)

    def answer_preview(self, obj):
        if obj.answer_text:
            return obj.answer_text[:40] + "..." if len(obj.answer_text) > 40 else obj.answer_text
        return "File uploaded" if obj.answer_file else "-"
    answer_preview.short_description = 'Answer'