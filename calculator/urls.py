from django.urls import path
from calculator import views

app_name = 'calculator'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]