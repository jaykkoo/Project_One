from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "application/home/home.html")

def about_us(request):
    return render(request, "application/home/about_us.html")

def contact_us(request):
    return render(request, "application/home/contact_us.html")