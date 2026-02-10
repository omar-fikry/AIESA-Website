from django.db import models
from django.utils import timezone

class Trustee(models.Model):
    POSITION_CHOICES = [
        ('chairperson', 'Chairperson'),
        ('vice_chairperson', 'Vice Chairperson'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('member', 'Board Member'),
        ('advisor', 'Advisor'),
        ('ex_officio', 'Ex-Officio Member'),
    ]
    
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='member')
    custom_position = models.CharField(max_length=100, blank=True, help_text="If 'Other' is selected")
    
    bio = models.TextField(help_text="Professional biography")
    short_bio = models.TextField(max_length=300, blank=True, help_text="Brief introduction (for cards)")
    
    photo = models.ImageField(upload_to='trustees/photos/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # Professional info
    current_role = models.CharField(max_length=200, blank=True, verbose_name="Current Position")
    organization = models.CharField(max_length=200, blank=True)
    qualifications = models.TextField(blank=True, help_text="Degrees and certifications")
    
    # Social links
    linkedin = models.URLField(blank=True)
    google_scholar = models.URLField(blank=True)
    researchgate = models.URLField(blank=True)
    website = models.URLField(blank=True)
    
    # Tenure
    term_start = models.DateField(default=timezone.now)
    term_end = models.DateField(blank=True, null=True)
    
    # Display settings
    is_active = models.BooleanField(default=True)
    is_current = models.BooleanField(default=True, verbose_name="Currently Serving")
    show_on_website = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Trustee"
        verbose_name_plural = "Trustees"
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"
    
    @property
    def display_position(self):
        return self.custom_position if self.custom_position else self.get_position_display()

class BoardTerm(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., 2023-2025 Board")
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    members = models.ManyToManyField(Trustee, related_name='board_terms', blank=True)
    
    class Meta:
        ordering = ['-start_year']
    
    def __str__(self):
        return self.name
