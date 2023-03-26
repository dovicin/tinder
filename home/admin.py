from django.contrib import admin

from .models import Question
from .models import Choice

admin.site.site_header = "Admin Page"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Soru Bilgisi', {'fields': ['question_text'], 'classes': ["collapse"]}),
        ('Tarih Bilgisi',{'fields': ['pub_date'], 'classes': ["collapse"]}),    
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question)
admin.site.register(Choice)