from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse("Hello world from Django!")


def greeting(request):
    return HttpResponse("Hello! Today is a <h1>great</h1> day to change the world and make it <h1>better!</h1>")


def introduction(request):
    return HttpResponse("Here you can find your motivation and share your thoughts with other users.")


def currenttime(request):
    currtime = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    return HttpResponse(f"Here you can see current date and time: <br> <h1>{currtime}</h1>")


def task(request):
    return redirect(solution)


def solution(request):
    my_dict = dict()
    for i in range(1, 16):
        key = i
        value = i ** 2
        my_dict[key] = value
    return HttpResponse(f"The solution of your task is this dictionary: {my_dict}")
