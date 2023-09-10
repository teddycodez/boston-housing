"""housing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
# Serving Static Files in development
from django.conf.urls.static import static
from django.conf import settings


# Admin site editt
admin.site.site_header  =  "Boston Housing Price Prediction Admin"  
admin.site.site_title  =  "Boston Housing Price Prediction Admin site"
admin.site.index_title  =  "Boston Housing Price Prediction Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("housing.url"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
