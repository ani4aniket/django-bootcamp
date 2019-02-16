from django.shortcuts import render

# Create your views here.

from .models import Student


def StudentListView(request):
    students= Student.objects.all()
    return render(request,
                  'student_list.html',
                  {'all_students':students})


def StudentDetailView(request,pk):
    std= Student.objects.get(id=pk)

    return render(request,'students_details.html',{'student':std})
