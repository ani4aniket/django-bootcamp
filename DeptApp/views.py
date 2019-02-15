from django.shortcuts import render

# Create your views here.

from .models import Student


def StudentDetailView(request):
    students= Student.objects.all()
    return render(request,
                  'students.html',
                  {'all_students':students})