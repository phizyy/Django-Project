from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name': 'Shijun',
        'age': '14',
    }
    return render(request, 'index.html', context)
