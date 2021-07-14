from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def canvas(request):
    return render(request, 'coloring/canvas.html')