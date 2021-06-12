from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='index'),
    path('homepage',views.dashboard,name='homepage'),
    path('events',views.events,name='events'),
    path('student',views.student,name='student'),
    path('curriculam',views.curriculam,name='curriculam'),
    path('faculty',views.faculty,name='faculty'),
    path('profile',views.profile,name='profile'),
    path('activities',views.activities,name='activities'),
    path('login',views.login,name='login'),
    path('registration',views.register,name='registration'),
    path('attendance',views.attendance,name='attendance'),
    path('report',views.report,name='report'),
    path('lesson',views.lesson,name='lesson'),
    path('teacherdashboard',views.teacherdashboard,name='teacherdashboard'),    
    path('addexam',views.addexam,name='addexam'),
    path('addassignment',views.addassignment,name='addassignment'),
    path('addtutorial',views.addtutorial,name='addtutorial'),
    path('addevent',views.addevent,name='addevent'),

]
