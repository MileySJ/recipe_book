from django.shortcuts import render, get_object_or_404
from .models import Asian, Italian


def home(request):
    return render(request, 'recipes/home.html')

def asian(request):
    asians = Asian.objects.all()
    return render(request, 'recipes/asian.html', {'asians':asians})

def asian_detail(request, asian_id):
    asian = get_object_or_404(Asian, pk=asian_id)
    return render(request, 'recipes/asian_detail.html', {'asian':asian})

def italian(request):
    italians = Italian.objects.all()
    return render(request, 'recipes/italian.html', {'italians':italians})

def italian_detail(request, italian_id):
    italian = get_object_or_404(Italian, pk=italian_id)
    return render(request, 'recipes/italian_detail.html', {'italian':italian})