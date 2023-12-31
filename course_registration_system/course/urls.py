from django.urls import path
from . import views

urlpatterns = [
    path('course/list/', views.course_list, name='course_list'),
    path('course/add/', views.course_add, name='course_add'),
    path('course/delete/', views.course_delete, name='course_delete'),
    path('course/add_button/',views.add_seat,name='add_seat'),
    path('course/drop_button/',views.drop_seat,name='drop_seat'),
]