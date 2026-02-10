from django.db import models
from django.utils import timezone
from django.urls import reverse

class TrainingProgram(models.Model):
    TYPE_CHOICES = [
        ('workshop', 'Workshop'),
        ('certificate', 'Certificate Program'),
        ('short_course', 'Short Course'),
        ('webinar', 'Webinar Series'),
        ('seminar', 'Seminar'),
        ('internship', 'Internship Program'),
        ('fellowship', 'Research Fellowship'),
    ]
    
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('all_levels', 'All Levels'),
    ]
    
    MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'In-Person'),
        ('hybrid', 'Hybrid'),
        ('self_paced', 'Self-Paced'),
    ]
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('registration_open', 'Registration Open'),
        ('registration_closed', 'Registration Closed'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    program_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='workshop')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='all_levels')
    
    short_description = models.TextField(max_length=300)
    detailed_description = models.TextField()
    learning_objectives = models.TextField(help_text="What participants will learn")
    target_audience = models.TextField(help_text="Who should attend")
    
    # Schedule
    start_date = models.DateField()
    end_date = models.DateField()
    registration_deadline = models.DateField(blank=True, null=True)
    schedule = models.TextField(blank=True, help_text="Detailed schedule")
    
    # Logistics
    mode = models.CharField(max_length=20, choices=MODE_CHOICES, default='online')
    venue = models.TextField(blank=True, help_text="For offline/hybrid programs")
    online_link = models.URLField(blank=True, verbose_name="Online Session Link")
    
    # Fees and Registration
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fee_currency = models.CharField(max_length=3, default='USD')
    fee_description = models.TextField(blank=True, help_text="What's included in fee")
    early_bird_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    early_bird_deadline = models.DateField(blank=True, null=True)
    
    registration_link = models.URLField(blank=True)
    max_participants = models.IntegerField(blank=True, null=True)
    current_participants = models.IntegerField(default=0)
    
    # Resources
    brochure = models.FileField(upload_to='training/brochures/', blank=True, null=True)
    syllabus = models.FileField(upload_to='training/syllabi/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='training/covers/', blank=True, null=True)
    
    # Instructors/Facilitators
    instructors = models.TextField(help_text="Names and affiliations of instructors")
    
    # Certification
    provides_certificate = models.BooleanField(default=True)
    certificate_name = models.CharField(max_length=200, blank=True)
    accreditation = models.TextField(blank=True)
    
    # Status and display
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'title']
        verbose_name = "Training Program"
        verbose_name_plural = "Training Programs"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('training_detail', kwargs={'slug': self.slug})
    
    @property
    def is_upcoming(self):
        return self.start_date > timezone.now().date()
    
    @property
    def is_ongoing(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date
    
    @property
    def registration_status(self):
        if self.status == 'registration_open':
            return 'open'
        elif self.status == 'registration_closed':
            return 'closed'
        elif self.is_upcoming:
            return 'upcoming'
        else:
            return 'closed'
    
    @property
    def seats_available(self):
        if self.max_participants:
            return max(0, self.max_participants - self.current_participants)
        return None

class TrainingResource(models.Model):
    training = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='training/resources/')
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} - {self.training.title}"
