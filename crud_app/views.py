from django.shortcuts import render
from .forms import StudentForm
from . models import Student
from django.http import  HttpResponseRedirect
# Create your views here.
def home(request):
    qyery = Student.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = StudentForm()
    return render(request, 'crud_app/index.html',{"form": form,"qyery":qyery})

def edit(request, id):
    qyery = Student.objects.all()
    query_e = Student.objects.get(pk = id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = query_e)
        if form.is_valid():
            form.save()
        form = StudentForm()
        return render(request, 'crud_app/index.html',{"form": form,"qyery":qyery})
    form = StudentForm(instance = query_e)
    return render(request, 'crud_app/edit.html',{"form": form})

def delete(request, id):
    qyery_d = Student.objects.get(id = id)
    qyery_d.delete()
    form = StudentForm()
    qyery = Student.objects.all()
    return HttpResponseRedirect('/')