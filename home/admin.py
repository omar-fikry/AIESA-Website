from django.contrib import admin
from .models import Organization, SiteSetting , News

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('nav_item', 'url_name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ('order',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'summary')