from django.contrib import admin
from .models import Teacher, CourseCategory, Course, Student

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(Student)



