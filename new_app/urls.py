from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "HomePage"),
    path('greeting', views.greeting, name = "GreetingUser"),
    path('introduction', views.introduction, name = "Intro"),
    path('currenttime', views.currenttime, name = "DateTime"),
    path('task', views.task, name = "TaskSolution"),
    path('solution', views.solution, name = "Solution")

]