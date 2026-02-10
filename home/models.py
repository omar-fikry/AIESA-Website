from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200, default="AIESA")
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organization"

class SiteSetting(models.Model):
    nav_item = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nav_item
    
    class Meta:
        ordering = ['order']
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"


################################################################
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان")
    summary = models.TextField(max_length=500, verbose_name="ملخص الخبر")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="صورة الخبر")
    created_at = models.DateTimeField(auto_now_add=True,db_index=True, verbose_name="تاريخ النشر")

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
