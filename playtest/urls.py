"""playtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from books.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('calculator/', include('calculator.urls')),
    path('vuejs/', TemplateView.as_view(template_name="start_vue.html"), name='start_vuejs'),
    path('admin/', admin.site.urls),
]
