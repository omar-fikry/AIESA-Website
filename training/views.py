from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import TrainingProgram

def training(request):
    now = timezone.now().date()
    
    # Filter programs
    upcoming_programs = TrainingProgram.objects.filter(
        status__in=['upcoming', 'registration_open'],
        start_date__gte=now,
        is_active=True
    ).order_by('start_date')
    
    ongoing_programs = TrainingProgram.objects.filter(
        status='ongoing',
        is_active=True
    ).order_by('start_date')
    
    past_programs = TrainingProgram.objects.filter(
        status='completed',
        is_active=True
    ).order_by('-start_date')
    
    featured_programs = TrainingProgram.objects.filter(
        is_featured=True,
        is_active=True
    ).order_by('-start_date')
    
    # Group by type
    workshops = TrainingProgram.objects.filter(
        program_type='workshop',
        is_active=True
    ).order_by('-start_date')
    
    certificate_programs = TrainingProgram.objects.filter(
        program_type='certificate',
        is_active=True
    ).order_by('-start_date')
    
    context = {
        'title': 'Training Programs',
        'upcoming_programs': upcoming_programs,
        'ongoing_programs': ongoing_programs,
        'past_programs': past_programs,
        'featured_programs': featured_programs,
        'workshops': workshops,
        'certificate_programs': certificate_programs,
    }
    return render(request, 'training/index.html', context)

def training_detail(request, slug):
    program = get_object_or_404(TrainingProgram, slug=slug, is_active=True)
    resources = program.resources.filter(is_public=True)
    
    context = {
        'title': program.title,
        'program': program,
        'resources': resources,
    }
    return render(request, 'training/detail.html', context)
