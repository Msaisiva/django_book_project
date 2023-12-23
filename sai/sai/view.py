from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def formvalidation(request):
    return render(request, 'formvalidation.html')