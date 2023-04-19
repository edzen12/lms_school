from django.db import models


# Teacher Model
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    skills=models.TextField()

    class Meta:
        verbose_name_plural = "1. Учителя"

    def __str__(self) -> str:
        return self.full_name


# Course Category Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()

    class Meta:
        verbose_name_plural = "2. Категории Курса"

    def __str__(self) -> str:
        return self.title


# Course Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    featured_img = models.ImageField(upload_to='course_img/', null=True)
    techs=models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3. Курсы"
    
    def __str__(self) -> str:
        return self.title

    

# Student Model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    address=models.TextField()
    interested_categories=models.TextField()

    class Meta:
        verbose_name_plural = "4. Студенты"
    
    def __str__(self) -> str:
        return self.full_name