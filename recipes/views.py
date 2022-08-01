from django.shortcuts import render
from .models import Asian, Italian


def home(request):
    return render(request, 'recipes/home.html', name='home')

def asian(request):
    asians = Asian.objects.all()
    return render(request, 'recipes/asian.html', {'asians':asians})

def italian(request):
    italians = Italian.objects.all()
    return render(request, 'recipes/italian.html', {'italians':italians})