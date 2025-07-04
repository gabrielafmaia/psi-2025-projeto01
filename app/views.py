from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def elenco(request):
    return render(request, 'app/elenco.html')

def sobre(request):
    return render(request, 'app/sobre.html')