from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice

admin.site.site_header = "AnimePoll"
admin.site.site_title = "AnimePoll Admin Area"
admin.site.index_title = "Welcome to AnimePoll Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [(None,{'field':['question_text']}),
    ('Date Information',{'field': ['pub_date'],'classes' : ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)
