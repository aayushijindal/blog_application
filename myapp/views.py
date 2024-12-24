from django.shortcuts import render,redirect
from .models import Homepage
# Import the PartyForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def main(request):
    home = Homepage.objects.all()
    return render(request, 'home.html')
