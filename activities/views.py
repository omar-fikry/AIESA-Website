from django.shortcuts import render, get_object_or_404
from .models import ScientificActivity

def activities(request):
    # Filter activities
    ongoing_activities = ScientificActivity.objects.filter(
        status='ongoing',
        show_on_website=True
    ).order_by('-start_date')
    
    completed_activities = ScientificActivity.objects.filter(
        status='completed',
        show_on_website=True
    ).order_by('-start_date')
    
    upcoming_activities = ScientificActivity.objects.filter(
        status='upcoming',
        show_on_website=True
    ).order_by('start_date')
    
    featured_activities = ScientificActivity.objects.filter(
        is_featured=True,
        show_on_website=True
    ).order_by('-start_date')
    
    # Group by type
    research_projects = ScientificActivity.objects.filter(
        activity_type='research',
        show_on_website=True
    ).order_by('-start_date')
    
    outreach_activities = ScientificActivity.objects.filter(
        activity_type='public_outreach',
        show_on_website=True
    ).order_by('-start_date')
    
    context = {
        'title': 'Scientific Activities',
        'ongoing_activities': ongoing_activities,
        'completed_activities': completed_activities,
        'upcoming_activities': upcoming_activities,
        'featured_activities': featured_activities,
        'research_projects': research_projects,
        'outreach_activities': outreach_activities,
    }
    return render(request, 'activities/index.html', context)

def activity_detail(request, slug):
    activity = get_object_or_404(ScientificActivity, slug=slug, show_on_website=True)
    photos = activity.photos.all().order_by('order')
    updates = activity.updates.all().order_by('-date')
    
    context = {
        'title': activity.title,
        'activity': activity,
        'photos': photos,
        'updates': updates,
    }
    return render(request, 'activities/detail.html', context)
