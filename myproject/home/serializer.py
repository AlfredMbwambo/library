from  home.models import Student
from  home.models import Loan_book
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields= ['full_name']

class Loan_booktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_book
        fields= ['name_book_borrowed','status','remarks']        

class pull_all_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields= ['full_name','registration_number']

class pull_all_booksborrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_book
        fields= ['name_book_borrowed','status']                

class pull_all_booksnotreturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_book
        fields= ['name_book_borrowed','status']    
