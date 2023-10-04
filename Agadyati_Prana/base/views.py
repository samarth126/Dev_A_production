from django.shortcuts import render

# Create your views here.

def booking(request):
    return render(request, 'main_site/Appointment.html')

def index(request):
    return render(request, 'main_site/index.html')

def about(request):
    return render(request, 'main_site/about.html')

def main_admin(request):
    return render(request, 'admin_site/index.html')

def form_admin(request):
    return render(request, 'admin_site/forms-advanced-form.html')

def business_unit(request):
    return render(request, 'main_site/business_unit.html')


def retreat(request):
    return render(request, 'main_site/retreat.html')


def offering(request):
    return render(request, 'main_site/offerings.html' )
