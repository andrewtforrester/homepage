from django.shortcuts import render

def home(request):
    context = {

    }

    return render(request, 'psite/home.html', context)
