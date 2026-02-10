from django.shortcuts import render
from .models import News

def home(request):
    latest_news = News.objects.all()[:3]

    context = {
        'title': 'Home',
        'latest_news': latest_news,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    return render(request, 'home/contact.html', {
        'title': 'Contact Us',
        'organization': {
            'email': 'search.aiesa@gmail.com',
            'phone': '+20 115 693 9552',
        }
    })
