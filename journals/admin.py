from django.contrib import admin
from .models import Journal, Volume

class VolumeInline(admin.TabularInline):
    model = Volume
    extra = 0
    fields = ['volume_number', 'year', 'issue_number', 'published_date', 'is_published']
    ordering = ['-year', '-volume_number']

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'issn', 'frequency', 'status', 'order', 'is_featured', 'created_at']
    list_filter = ['status', 'is_featured', 'frequency']
    search_fields = ['title', 'issn', 'description']
    list_editable = ['status', 'order', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'short_description', 'cover_image')
        }),
        ('Publication Details', {
            'fields': ('issn', 'frequency', 'publisher', 'editor_in_chief', 'impact_factor')
        }),
        ('Indexing & Links', {
            'fields': ('indexing', 'submission_link', 'website_link')
        }),
        ('Display Settings', {
            'fields': ('status', 'order', 'is_featured')
        }),
    )
    inlines = [VolumeInline]

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ['journal', 'volume_number', 'year', 'issue_number', 'published_date', 'is_published']
    list_filter = ['journal', 'year', 'is_published']
    search_fields = ['journal__title', 'volume_number']
    list_editable = ['is_published']