from django.contrib import admin
from .models import Trustee, BoardTerm

class TrusteeInline(admin.TabularInline):
    model = BoardTerm.members.through
    extra = 0
    verbose_name = "Trustee"
    verbose_name_plural = "Trustees"

@admin.register(Trustee)
class TrusteeAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_position', 'organization', 'is_current', 'show_on_website', 'order']
    list_filter = ['position', 'is_current', 'show_on_website', 'term_start', 'term_end']
    search_fields = ['name', 'bio', 'current_role', 'organization']
    list_editable = ['is_current', 'show_on_website', 'order']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'photo', 'bio', 'short_bio')
        }),
        ('Position Details', {
            'fields': ('position', 'custom_position', 'is_current', 'order')
        }),
        ('Professional Information', {
            'fields': ('current_role', 'organization', 'qualifications')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'google_scholar', 'researchgate', 'website')
        }),
        ('Term Information', {
            'fields': ('term_start', 'term_end')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'show_on_website')
        }),
    )

@admin.register(BoardTerm)
class BoardTermAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_year', 'end_year', 'is_current']
    list_filter = ['is_current']
    search_fields = ['name', 'description']
    list_editable = ['is_current']
    
    filter_horizontal = ['members']
    
    fieldsets = (
        ('Term Information', {
            'fields': ('name', 'start_year', 'end_year', 'is_current', 'description')
        }),
        ('Board Members', {
            'fields': ('members',)
        }),
    )
