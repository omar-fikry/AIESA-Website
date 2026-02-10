from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Conference

def conferences(request):
    now = timezone.now().date()
    













    # Get conferences by status
    upcoming_conferences = Conference.objects.filter(
        status='upcoming', 
        start_date__gte=now
    ).order_by('start_date')
    
    ongoing_conferences = Conference.objects.filter(
        status='ongoing'
    ).order_by('start_date')
    
    past_conferences = Conference.objects.filter(
        status='completed'
    ).order_by('-start_date')
    
    featured_conferences = Conference.objects.filter(
        is_featured=True
    ).order_by('-start_date')
    
    context = {
        'title': 'Foundation Conferences',
        'upcoming_conferences': upcoming_conferences,
        'ongoing_conferences': ongoing_conferences,
        'past_conferences': past_conferences,
        'featured_conferences': featured_conferences,
    }
    return render(request, 'conferences/index.html', context)

def conference_detail(request, slug):
    conference = get_object_or_404(Conference, slug=slug)
    speakers = conference.speakers.all().order_by('order')
    
    context = {
        'title': conference.title,
        'conference': conference,
        'speakers': speakers,
    }
    return render(request, 'conferences/detail.html', context)