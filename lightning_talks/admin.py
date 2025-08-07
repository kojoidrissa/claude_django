from django.contrib import admin
from .models import LightningTalk


@admin.register(LightningTalk)
class LightningTalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speaker_name', 'email', 'is_accepted', 'submitted_at', 'reviewed_at')
    list_filter = ('is_accepted', 'submitted_at', 'reviewed_at')
    search_fields = ('title', 'speaker_name', 'email', 'description')
    readonly_fields = ('submitted_at', 'updated_at')
    
    fieldsets = (
        ('Speaker Information', {
            'fields': ('speaker_name', 'email')
        }),
        ('Talk Details', {
            'fields': ('title', 'description')
        }),
        ('Review Status', {
            'fields': ('is_accepted', 'reviewed_at', 'notes')
        }),
        ('Timestamps', {
            'fields': ('submitted_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['accept_talks', 'reject_talks']
    
    def accept_talks(self, request, queryset):
        count = 0
        for talk in queryset:
            talk.accept()
            count += 1
        self.message_user(request, f'Successfully accepted {count} talk(s).')
    accept_talks.short_description = 'Accept selected talks'
    
    def reject_talks(self, request, queryset):
        count = 0
        for talk in queryset:
            talk.reject()
            count += 1
        self.message_user(request, f'Successfully rejected {count} talk(s).')
    reject_talks.short_description = 'Reject selected talks'
