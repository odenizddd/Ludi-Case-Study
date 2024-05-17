from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_panel, name='info_panel'),
]