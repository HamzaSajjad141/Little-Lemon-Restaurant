from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


