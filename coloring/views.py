from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def home(request):
    return render(request, 'coloring/home.html')
def pages(request):
    return render(request, 'coloring/pages.html')
def npages(request):
    return render(request, 'coloring/npages.html')
def addedpages(request):
    return render(request, 'coloring/addedpages.html')