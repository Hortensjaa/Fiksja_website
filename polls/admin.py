from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    readonly_fields = ('votes',)


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'pub_date',)
    fieldsets = [
        (None, {'fields': ['question_text', 'author', 'pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'author')


admin.site.register(Question, QuestionAdmin)
