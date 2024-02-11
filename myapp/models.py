from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Student(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    house_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)

class Department(models.Model):
    department_name = models.CharField(max_length=100)

class Subject(models.Model):
    subject = models.CharField(max_length=100)

class Course(models.Model):
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE,default="")
    Course_name = models.CharField(max_length=100)
    Semester = models.CharField(max_length=100)

class Teachers(models.Model):
    name = models.CharField(max_length=100)
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE,default="")
    photo = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE,default="1")

class Office_staff(models.Model):
    office_staff_name = models.CharField(max_length=100)
    office_staff_photo = models.CharField(max_length=500)
    office_staff_phone_number = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    email_id = models.CharField(max_length=100)


class Notification(models.Model):
    date = models.CharField(max_length=100)
    notification = models.CharField(max_length=100)

class Complaint(models.Model):
    date = models.CharField(max_length=100)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    reply = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)

class Location(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    OFFICE_STAFF = models.ForeignKey(Office_staff, on_delete=models.CASCADE)

class Club_members(models.Model):
    CLUB = models.ForeignKey(Club, on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default='pending')

class Scholarship(models.Model):
    student_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Id_card(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE,default="1")
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE,default="")
    academic_year = models.CharField(max_length=100,default='0')
    file = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Bus_pass(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    DEPARTMENT = models.ForeignKey(Department,on_delete=models.CASCADE,default="")
    f_place = models.CharField(max_length=100,default='0')
    to_place = models.CharField(max_length=100,default='0')
    academic_year = models.CharField(max_length=100,default='0')
    file = models.CharField(max_length=500)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Attendance(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject =models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    day = models.CharField(max_length=100)