from django.contrib import admin
from .models import TrainingProgram, TrainingResource

class TrainingResourceInline(admin.TabularInline):
    model = TrainingResource
    extra = 0
    fields = ['title', 'file', 'description', 'is_public']
    ordering = ['title']

@admin.register(TrainingProgram)
class TrainingProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'program_type', 'level', 'start_date', 'status', 'mode', 'fee', 'is_featured']
    list_filter = ['program_type', 'level', 'status', 'mode', 'is_featured', 'start_date']
    search_fields = ['title', 'short_description', 'detailed_description', 'instructors']
    list_editable = ['status', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'detailed_description')
        }),
        ('Program Details', {
            'fields': ('program_type', 'level', 'learning_objectives', 'target_audience')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date', 'registration_deadline', 'schedule')
        }),
        ('Logistics', {
            'fields': ('mode', 'venue', 'online_link')
        }),
        ('Fees and Registration', {
            'fields': ('fee', 'fee_currency', 'fee_description', 'early_bird_fee', 
                      'early_bird_deadline', 'registration_link', 'max_participants', 
                      'current_participants')
        }),
        ('Instructors and Certification', {
            'fields': ('instructors', 'provides_certificate', 'certificate_name', 'accreditation')
        }),
        ('Resources', {
            'fields': ('cover_image', 'brochure', 'syllabus')
        }),
        ('Display Settings', {
            'fields': ('status', 'is_featured', 'is_active', 'order')
        }),
    )
    
    inlines = [TrainingResourceInline]

@admin.register(TrainingResource)
class TrainingResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'training', 'is_public']
    list_filter = ['is_public', 'training']
    search_fields = ['title', 'description', 'training__title']
