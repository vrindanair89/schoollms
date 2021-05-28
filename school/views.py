from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfunc1(request):
    return HttpResponse('hello world')
def dashboard(request):
    return render(request,'dashboard.html')