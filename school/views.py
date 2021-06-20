from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
def admindashboard(request):
    return render(request,'admin_dashboard.html')
def classmanagement(request):
    detail=Class.objects.all()
    return render(request,'classmanagement.html',{'key':detail})
    # return render(request,'classmanagement.html')


def sum(request):
    return render(request,'sum.html')
def findsum(request):
    fnum=request.GET['fnum']
    snum=request.GET['snum']
    sum=int(fnum)+int(snum)
    return render(request,'sum.html',{'sum':sum})
def cal(request):
    if(request.method=='POST'):
        fnum=request.POST['fnum']
        snum=request.POST['snum']
        sum=int(fnum)+int(snum)
        return render(request,'cal.html',{'sum':sum})
    return render(request,'sum.html')
def reg(request):
    if(request.method=='POST'):
        name=request.POST['name']
        place=request.POST['place']
        contact=request.POST['contact']
        data1=Demo(first_name=name,place=place,contact=contact)
        data1.save()
        return render(request,'reg.html',{'message':'Successfully registered'})
    return render(request,'reg.html')
def repo(request):
    detail=Demo.objects.all()
    return render(request,'report_demo.html',{'key':detail})