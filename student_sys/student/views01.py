from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student


# Create your views here.
def index(request):
    students=Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student=Student(
            name=cleaned_data['name'],
            sex=cleaned_data['sex'],
            email=cleaned_data['email'],
            profession=cleaned_data['profession'],
            qq=cleaned_data['qq'],
            phone=cleaned_data['phone'])
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        'students': students,
        'form': form,
    }
    return render(request, template_name='index.html',context=context)