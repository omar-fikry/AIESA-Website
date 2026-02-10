from django.db import models
from django.utils import timezone
from django.urls import reverse

class Journal(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('upcoming', 'Upcoming'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly name (e.g., 'journal-of-science')")
    issn = models.CharField(max_length=20, blank=True, verbose_name="ISSN")
    description = models.TextField()
    short_description = models.TextField(max_length=300, blank=True)
    cover_image = models.ImageField(upload_to='journals/covers/', blank=True, null=True)
    frequency = models.CharField(max_length=50, default="Monthly", 
                                help_text="e.g., Monthly, Quarterly, Bi-annual")
    publisher = models.CharField(max_length=200, blank=True)
    editor_in_chief = models.CharField(max_length=200, blank=True)
    impact_factor = models.CharField(max_length=50, blank=True)
    indexing = models.TextField(blank=True, help_text="Where the journal is indexed (Scopus, Web of Science, etc.)")
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    submission_link = models.URLField(blank=True, verbose_name="Manuscript Submission URL")
    website_link = models.URLField(blank=True, verbose_name="Journal Website")
    
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Journal"
        verbose_name_plural = "Journals"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('journal_detail', kwargs={'slug': self.slug})

class Volume(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='volumes')
    volume_number = models.IntegerField()
    year = models.IntegerField()
    issue_number = models.CharField(max_length=20, blank=True)
    published_date = models.DateField(default=timezone.now)
    cover_image = models.ImageField(upload_to='journals/volumes/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='journals/pdfs/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-year', '-volume_number']
        unique_together = ['journal', 'volume_number', 'issue_number']
    
    def __str__(self):
        return f"{self.journal.title} - Vol.{self.volume_number}, {self.year}"
