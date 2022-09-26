from django.contrib import admin

from .models import Record, Break


class BreakInline(admin.StackedInline):
    model = Break
    extra = 0


class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'category']}),
        ('Description', {'fields': ['description'], "classes": ['collapse']}),
    ]
    inlines = [BreakInline]
    list_display = ('title', 'category')


admin.site.register(Record, RecordAdmin)
