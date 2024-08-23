from django.shortcuts import render, get_object_or_404
from galeria.models import Phothography


def index(request):
    photos = Phothography.objects.order_by("phothography_date").filter(published=True)
    return render(request, 'galeria/index.html', {"cards": photos})

def imagem(request, photo_id):
    photo = get_object_or_404(Phothography, pk=photo_id)
    return render(request, 'galeria/imagem.html', {'phothography': photo})

def search(request):
    photos = Phothography.objects.order_by("phothography_date").filter(published=True)
    
    if "search" in request.GET:
        name_for_search = request.GET['search']
        if name_for_search:
            photos = photos.filter(name__icontains=name_for_search)
    
    return render(request, 'galeria/search.html', {"cards": photos})