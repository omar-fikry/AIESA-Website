from django.contrib import admin
from .models import Conference, ConferenceSpeaker

class SpeakerInline(admin.TabularInline):
    model = ConferenceSpeaker
    extra = 0
    fields = ['name', 'title', 'affiliation', 'photo', 'order']
    ordering = ['order']

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ['title', 'conference_type', 'status', 'start_date', 'end_date', 'venue', 'is_featured']
    list_filter = ['status', 'conference_type', 'is_featured', 'start_date']
    search_fields = ['title', 'description', 'venue', 'city']
    list_editable = ['status', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    










    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_title', 'description', 'short_description')
        }),
        ('Conference Details', {
            'fields': ('conference_type', 'status', 'theme', 'topics')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'abstract_deadline', 'registration_deadline', 'early_bird_deadline')
        }),
        ('Location', {
            'fields': ('venue', 'city', 'country', 'is_online', 'online_link')
        }),
        ('Links', {
            'fields': ('website', 'registration_link', 'submission_link')
        }),
        ('Contact Information', {
            'fields': ('organizers', 'contact_email', 'contact_phone')
        }),
        ('Media', {
            'fields': ('banner_image', 'brochure')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'order')
        }),
    )
    
    inlines = [SpeakerInline]

@admin.register(ConferenceSpeaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'conference', 'title', 'affiliation', 'order']
    list_filter = ['conference']
    search_fields = ['name', 'title', 'affiliation', 'conference__title']
    list_editable = ['order']