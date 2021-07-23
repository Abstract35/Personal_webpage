from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def business_view(request, *args, **kwargs):
    return render(request, "business.html", {})

def education_view(request, *args, **kwargs):
    return render(request, "education.html", {})

def experience_view(request, *args, **kwargs):
    return render(request, "experience.html", {})

def family_view(request, *args, **kwargs):
    return render(request, "family.html", {})

def interests_view(request, *args, **kwargs):
    return render(request, "interests.html", {})

def portfolio_view(request, *args, **kwargs):
    return render(request, "portfolio.html", {})

def products_view(request, *args, **kwargs):
    return render(request, "products.html", {})

def projects_view(request, *args, **kwargs):
    return render(request, "projects.html", {})

def skills_view(request, *args, **kwargs):
    return render(request, "skills.html", {})

def sports_view(request, *args, **kwargs):
    return render(request, "sports.html", {})

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")



