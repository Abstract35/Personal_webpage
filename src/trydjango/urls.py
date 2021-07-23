"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from pages.views import ( home_view, 
    contact_view, 
    about_view,
    business_view,
    education_view,
    experience_view,
    family_view,
    interests_view,
    portfolio_view,
    products_view,
    projects_view,
    skills_view,
    sports_view,
)

from products.views import (
        product_list_view,
        product_detail_view,
        product_delete_view,
        product_update_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about', about_view, name='about'),
    path('business/', business_view, name='business'),
    path('education/', education_view, name='education'),
    path('experience/', experience_view, name='experience'),
    path('family/', family_view, name='family'),
    path('interests/', interests_view, name='interests'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('products/', products_view, name='products'),
    path('projects/', projects_view, name='projects'),
    path('skills/', skills_view, name='skills'),
    path('sports/', sports_view, name='sports'),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/bootstrap.base.html')),
]



