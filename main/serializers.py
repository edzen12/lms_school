from rest_framework import serializers
from .models import Teacher, CourseCategory


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name','email','password','qualification','mobile_no','skills' ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id','title','description']