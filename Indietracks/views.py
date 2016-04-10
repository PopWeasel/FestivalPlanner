from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def performers(request):
    return render(request, 'performers.html', {
        'performerName': request.POST.get('performerName', "")})