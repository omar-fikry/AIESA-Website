from django.shortcuts import render, get_object_or_404
from .models import Journal

def journals(request):
    all_journals = Journal.objects.all()
    active_journals = Journal.objects.filter(status='active')
    featured_journals = Journal.objects.filter(is_featured=True, status='active')
    
    context = {
        'title': 'Foundation Journals',
        'all_journals': all_journals,
        'active_journals': active_journals,
        'featured_journals': featured_journals,
    }
    return render(request, 'journals/index.html', context)

def journal_detail(request, slug):
    journal = get_object_or_404(Journal, slug=slug)
    volumes = journal.volumes.filter(is_published=True).order_by('-year', '-volume_number')
    
    context = {
        'title': journal.title,
        'journal': journal,
        'volumes': volumes,
    }
    return render(request, 'journals/detail.html', context)
