from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name= 'home.html')

def about(request):
    return render(request, template_name= 'about.html')


def services(request):
    return render(request, template_name= 'services.html')

def contact (request):
    return render(request, template_name= 'contact.html')

def products(request):
    return render(request, template_name= 'products.html')
