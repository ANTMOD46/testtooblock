from django.urls import path 
from . views import *

urlpatterns = [
    path('mod/', course_list, name='course_list'),
    path('courseseach/', course_idsearch, name= 'course_idsearch'),
    path('coursenameseach/', course_nameseach, name= 'course_nameseach'),
    path('update/<str:pk>',CourseUpdateView.as_view(),name='course-update'),
    path('delete/<str:pk>',CourseDeleteView.as_view(), name='course-delete'),
    
    
    
    
    
]