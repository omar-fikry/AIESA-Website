from django.db import models
from django.utils import timezone
from django.urls import reverse

class Conference(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    TYPE_CHOICES = [
        ('international', 'International Conference'),
        ('national', 'National Conference'),
        ('workshop', 'Workshop'),
        ('symposium', 'Symposium'),
        ('webinar', 'Webinar'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly name")
    short_title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    short_description = models.TextField(max_length=300, blank=True)

    



    conference_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='international')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField()
    abstract_deadline = models.DateField(blank=True, null=True)
    registration_deadline = models.DateField(blank=True, null=True)
    early_bird_deadline = models.DateField(blank=True, null=True)
    
    # Location
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)
    online_link = models.URLField(blank=True, verbose_name="Online Conference Link")
    
    # Important URLs
    website = models.URLField(blank=True)
    registration_link = models.URLField(blank=True)
    submission_link = models.URLField(blank=True, verbose_name="Paper Submission Link")
    
    # Organizers
    organizers = models.TextField(blank=True, help_text="List of organizing committees")
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    # Additional info
    theme = models.CharField(max_length=300, blank=True)
    topics = models.TextField(blank=True, help_text="Conference topics (one per line)")
    
    # Media
    banner_image = models.ImageField(upload_to='conferences/banners/', blank=True, null=True)
    brochure = models.FileField(upload_to='conferences/brochures/', blank=True, null=True)
    
    # Display settings
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Display order")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['start_date', 'title']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('conference_detail', kwargs={'slug': self.slug})
    
    @property
    def is_upcoming(self):
        return self.start_date > timezone.now().date()
    
    @property
    def is_past(self):
        return self.end_date < timezone.now().date()
    
    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days + 1

class ConferenceSpeaker(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='speakers')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    affiliation = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='conferences/speakers/', blank=True, null=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.conference.short_title}"
