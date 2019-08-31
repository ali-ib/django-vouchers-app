from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='check', permanent=False), name='index'),
    path('check/', views.CheckView.as_view(), name='check'),
    path('result/', views.result_view, name='result'),
]