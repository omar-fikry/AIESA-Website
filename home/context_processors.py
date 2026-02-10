from .models import Organization, SiteSetting

def organization_info(request):
    # Get or create organization info
    org, created = Organization.objects.get_or_create(
        name="AIESA",
        defaults={
            'description': 'Scientific Publishing Organization',
            'email': 'contact@aiesa.org'
        }
    )
    
    # Get navigation items
    nav_items = SiteSetting.objects.filter(is_active=True)
    
    # If no navigation items exist, create default ones
    if not nav_items.exists():
        default_nav = [
            ('Home', 'home', 1),
            ('Board of Trustees', 'trustees', 2),
            ('Foundation Conferences', 'conferences', 3),
            ('Foundation Journals', 'journals', 4),
            ('Training', 'training', 5),
            ('Scientific Activity', 'activities', 6),
            ('Contact Us', 'contact', 7),
        ]
        
        for nav_name, url_name, order in default_nav:
            SiteSetting.objects.create(
                nav_item=nav_name,
                url_name=url_name,
                order=order
            )
        
        nav_items = SiteSetting.objects.filter(is_active=True)
    
    return {
        'organization': org,
        'nav_items': nav_items,
    }