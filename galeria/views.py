from django.shortcuts import render


def index(request):
    data = {
        1: {"name": "Nebulosa de Carina",
            "legend": "webbtelecope.org / NASA / James Webb"},
        2: {"name": "Galáxia NGC 1079",
            "legend": "nasa.org / NASA / Hubble"}
    }
    return render(request, 'galeria/index.html', {"cards": data})

def imagem(request):
    return render(request, 'galeria/imagem.html')