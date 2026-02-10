from django.shortcuts import render
from .models import Trustee, BoardTerm

def trustees(request):
    current_trustees = Trustee.objects.filter(
        is_current=True, 
        show_on_website=True
    ).order_by('order', 'name')
    
    past_trustees = Trustee.objects.filter(
        is_current=False,
        show_on_website=True
    ).order_by('-term_end', 'name')
    
    board_terms = BoardTerm.objects.all().order_by('-start_year')
    current_board = BoardTerm.objects.filter(is_current=True).first()
    
    context = {
        'title': 'Board of Trustees',
        'current_trustees': current_trustees,
        'past_trustees': past_trustees,
        'board_terms': board_terms,
        'current_board': current_board,
    }
    return render(request, 'trustees/index.html', context)

def trustee_detail(request, pk):
    from django.shortcuts import get_object_or_404
    trustee = get_object_or_404(Trustee, pk=pk, show_on_website=True)
    
    context = {
        'title': trustee.name,
        'trustee': trustee,
    }
    return render(request, 'trustees/detail.html', context)
