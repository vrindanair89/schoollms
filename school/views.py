from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')
def events(request):
    return render(request,'events.html')
def student(request):
    return render(request,'student.html')
def curriculam(request):
    return render(request,'curriculam.html')
def faculty(request):
    return render(request,'faculty.html')
def profile(request):
    return render(request,'profile.html')
def activities(request):
    return render(request,'activities.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'registration.html')
def attendance(request):
    return render(request,'attendance.html')
def report(request):
    return render(request,'report.html')

