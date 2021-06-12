from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'samplesite.html')
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
def lesson(request):
    return render(request,'lessonsdashboard.html')
def teacherdashboard(request):
    return render(request,'teacherdashboard.html')
def addexam(request):
    return render(request,'addexam.html')  
def addassignment(request):
    return render(request,'teacher_assignment.html') 
def addtutorial(request):
    return render(request,'teacher_tutorial.html')
def addevent(request):
    return render(request,'teacher_event.html')