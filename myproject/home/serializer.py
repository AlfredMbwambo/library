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
