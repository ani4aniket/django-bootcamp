from django.urls import path

from .views import StudentDetailView
urlpatterns = [
    path('',StudentDetailView,name='std')
]
