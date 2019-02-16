from django.urls import path

from .views import StudentDetailView,StudentListView
urlpatterns = [
    path('',StudentListView,name='std_list'),

    path('<int:pk>/',StudentDetailView,name='std_detail')
]
