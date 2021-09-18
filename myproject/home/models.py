from django.db import models

from django.db import models


class Librarian(models.Model):
    librarian_id = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True)

    librarians = models.Manager()

    class Meta:
        db_table = "librarians"

class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    full_name= models.CharField(max_length=150)
    registration_number = models.CharField(max_length=150)
    standard = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    registered = models.DateTimeField(auto_now_add=True)

    students = models.Manager()

    class Meta:
        db_table = "students"

class Loan_book(models.Model):
    nam_book_borrowed_id = models.CharField(max_length=50, primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    name_book_borrowed = models.CharField(max_length=150)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=False)
    remarks = models.CharField(max_length=150)
    loan_books = models.Manager()

    class Meta:
        db_table = "loan_books"                  
