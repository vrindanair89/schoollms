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
    
    
]