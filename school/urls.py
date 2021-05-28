from django.urls import path
from . import views
urlpatterns = [
    path('test1',views.testfunc1,name='test1'),
    path('home',views.dashboard,name='home'),
]