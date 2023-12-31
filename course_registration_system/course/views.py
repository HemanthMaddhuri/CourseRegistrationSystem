from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Course

def course_list(request):
    mycourse = Course.objects.all()
    return render(request, "course_list.html", {"mycourse":mycourse})

def course_add(request):
    if request.method == "GET":
        return render(request, "course_add.html")

    course_id = request.POST.get("course_id")
    title = request.POST.get("title")
    instructor = request.POST.get("instructor")
    capacity = 30
    open_seats = 30
    Course.objects.create(course_id=course_id, title=title, instructor=instructor, capacity=capacity, open_seats=open_seats)
    return redirect("/course/list/")

def course_delete(request):
    c_id = request.GET.get("course_id")
    Course.objects.filter(course_id=c_id).delete()
    return redirect("/course/list/")

def add_seat(request):
    course_id = request.GET.get("course_id")
    course = Course.objects.get(course_id=course_id)
    if course.open_seats > 0:
        course.open_seats -= 1
        course.save()
    return redirect("/course/list/")

def drop_seat(request):
    course_id = request.GET.get("course_id")
    course = Course.objects.get(course_id=course_id)
    course.open_seats = min(course.open_seats + 1, course.capacity)
    course.save()
    return redirect("/course/list/")