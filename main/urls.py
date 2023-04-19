from django.urls import path 
from .views import TeacherList, TeacherDetail, teacher_login, CategoryList


urlpatterns = [
    #Teacher
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/', TeacherDetail.as_view()),
    path('teacher-login', teacher_login),
    #Teacher
    path('category/', CategoryList.as_view()),
]
