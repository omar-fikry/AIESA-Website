from django.db import models
from django.utils import timezone
from django.urls import reverse

class ScientificActivity(models.Model):
    TYPE_CHOICES = [
        ('research', 'Research Project'),
        ('collaboration', 'Research Collaboration'),
        ('public_outreach', 'Public Outreach'),
        ('community_service', 'Community Service'),
        ('student_program', 'Student Program'),
        ('award', 'Award/Grant'),
        ('partnership', 'Partnership'),
        ('event', 'Special Event'),
        ('publication', 'Special Publication'),
        ('other', 'Other Activity'),
    ]
    
    STATUS_CHOICES = [
        ('planning', 'In Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('suspended', 'Suspended'),
        ('upcoming', 'Upcoming'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    activity_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    
    short_description = models.TextField(max_length=300)
    detailed_description = models.TextField()
    
    # Timeline
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    
    # Participants
    principal_investigator = models.CharField(max_length=200, blank=True)
    collaborators = models.TextField(blank=True, help_text="Names and institutions")
    participants_count = models.IntegerField(blank=True, null=True)
    
    # Funding
    funding_source = models.TextField(blank=True)
    grant_number = models.CharField(max_length=100, blank=True)
    budget = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    # Location
    location = models.CharField(max_length=200, blank=True)
    is_virtual = models.BooleanField(default=False)
    
    # Media
    cover_image = models.ImageField(upload_to='activities/covers/', blank=True, null=True)
    gallery_folder = models.CharField(max_length=100, blank=True, help_text="Folder name for activity photos")
    
    # Outcomes
    objectives = models.TextField(blank=True, help_text="Activity objectives")
    expected_outcomes = models.TextField(blank=True)
    achieved_outcomes = models.TextField(blank=True, help_text="Results and impact")
    publications = models.TextField(blank=True, help_text="Resulting publications")
    
    # Links
    website = models.URLField(blank=True)
    report = models.FileField(upload_to='activities/reports/', blank=True, null=True)
    
    # Status and display
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    is_featured = models.BooleanField(default=False)
    show_on_website = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-start_date', 'title']
        verbose_name = "Scientific Activity"
        verbose_name_plural = "Scientific Activities"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('activity_detail', kwargs={'slug': self.slug})
    
    @property
    def duration_months(self):
        if self.end_date and self.start_date:
            delta = self.end_date - self.start_date
            return delta.days // 30
        return None

class ActivityPhoto(models.Model):
    activity = models.ForeignKey(ScientificActivity, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='activities/photos/')
    caption = models.CharField(max_length=200, blank=True)
    photographer = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Photo for {self.activity.title}"

class ActivityUpdate(models.Model):
    activity = models.ForeignKey(ScientificActivity, on_delete=models.CASCADE, related_name='updates')
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    attachment = models.FileField(upload_to='activities/updates/', blank=True, null=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} - {self.date}"
