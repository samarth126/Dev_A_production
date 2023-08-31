from django.shortcuts import render

# Create your views here.
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