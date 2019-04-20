from django.shortcuts import render

# Create your views here.


def wiki_home(request):
    return render(request, 'index.html')
