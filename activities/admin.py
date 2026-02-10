from django.contrib import admin
from .models import ScientificActivity, ActivityPhoto, ActivityUpdate

class ActivityPhotoInline(admin.TabularInline):
    model = ActivityPhoto
    extra = 0
    fields = ['image', 'caption', 'photographer', 'order']
    ordering = ['order']

class ActivityUpdateInline(admin.TabularInline):
    model = ActivityUpdate
    extra = 0
    fields = ['title', 'content', 'date', 'attachment']
    ordering = ['-date']

@admin.register(ScientificActivity)
class ScientificActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'status', 'start_date', 'end_date', 'is_featured', 'show_on_website']
    list_filter = ['activity_type', 'status', 'is_featured', 'show_on_website', 'start_date']
    search_fields = ['title', 'short_description', 'detailed_description', 'principal_investigator']
    list_editable = ['status', 'is_featured', 'show_on_website']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'activity_type', 'short_description', 'detailed_description')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'is_ongoing')
        }),
        ('Participants', {
            'fields': ('principal_investigator', 'collaborators', 'participants_count')
        }),
        ('Funding', {
            'fields': ('funding_source', 'grant_number', 'budget')
        }),
        ('Location', {
            'fields': ('location', 'is_virtual')
        }),
        ('Objectives and Outcomes', {
            'fields': ('objectives', 'expected_outcomes', 'achieved_outcomes', 'publications')
        }),
        ('Media and Resources', {
            'fields': ('cover_image', 'gallery_folder', 'website', 'report')
        }),
        ('Display Settings', {
            'fields': ('status', 'is_featured', 'show_on_website', 'order')
        }),
    )
    
    inlines = [ActivityPhotoInline, ActivityUpdateInline]

@admin.register(ActivityPhoto)
class ActivityPhotoAdmin(admin.ModelAdmin):
    list_display = ['activity', 'caption', 'photographer', 'order']
    list_filter = ['activity']
    search_fields = ['caption', 'photographer', 'activity__title']
    list_editable = ['order']

@admin.register(ActivityUpdate)
class ActivityUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity', 'date']
    list_filter = ['date', 'activity']
    search_fields = ['title', 'content', 'activity__title']
