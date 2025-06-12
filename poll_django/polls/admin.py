from django.contrib import admin
from .models  import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Text", {"fields": ["question_text"]}),
        # ("Choices", {"fields": ["CHOICES"],"classes" : ["collapse"]}),
        ("Date information", {"fields": ["pub_date"],"classes" : ["collapse"]}),
    ]
    list_display = ["question_text","pub_date","was_published_recently"]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    # search_fields = ["polls"]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


