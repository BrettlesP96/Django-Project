from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here
@login_required
def home(request):
    return render(request, 'homepage.html')

@login_required
def discography(request):
    return render(request, 'discography.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact_us(request):
    return render(request, 'contact.html')
