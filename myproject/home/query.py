from  home.models import Librarian
from  home.models import Student
from  home.models import Loan_book
from  home.serializer import StudentSerializer
from  home.serializer import Loan_booktSerializer

import json

import uuid

def Librarian_registration(data):
  if not Librarian.librarians.filter(phone_number=data['phone_number']).exists():     
    new_user = Librarian()
    new_user.librarian_id = uuid.uuid4()
    new_user.full_name = data["full_name"]
    new_user.phone_number = data["phone_number"]
    new_user.password = data["password"]
    new_user.save()
    return json.dumps({'code':200,
                        "msg": "Librarian Registered"})
  else:
     return json.dumps({'code': 300,
                        "msg": "Phone number arleady exist"})                       

def Librarian_login(data):
  if Librarian.librarians.filter(phone_number=data['phone_number']).exists():
    librarian = Librarian.librarians.get(phone_number=data['phone_number'])
    if librarian.password == data['password']:
      return json.dumps({'code': 200,
                          "full_name": librarian.full_name,
                          "msg": "Librarian successfuly login"})
    else:
      return json.dumps({'code': 300,
                          "msg": "Incorrect Password"})
  else:
     return json.dumps({'code': 300,
                        "msg": "Name is arleady exist"})                                              

def student_registration(data):
  if not Student.students.filter(full_name=data['full_name']).exists():    
    new_student = Student()
    new_student.student_id = uuid.uuid4()
    new_student.full_name = data['full_name']
    new_student.registration_number = data["registration_number"]
    new_student.standard = data["standard"]
    new_student.gender = data["gender"]
    new_student.save()
    return json.dumps({'code':200,
                        "msg": "Student information successfuly stored"})
  else:
        return json.dumps({'code': 300,
                       "msg": "Student name is arleady exist"}) 

#apa ni kufetch jina tuu la mwanafunzi au taarifa alizo jisajiria katika mfumo huu
def search_student_name(data):
  query = data['registration_number']
  name= Student.students.filter(registration_number__icontains=query)
  count = name.count()
  Name = StudentSerializer(name, many=True).data

  return json.dumps({'code': 200, "name": Name})                                                

#taarifa za kitabu cha mwanafunzi anacho azima
def borrow_book(data):    
    new_book_infor = Loan_book()
    new_book_infor.nam_book_borrowed_id = uuid.uuid4()
    new_book_infor.student_id = data['student_id']
    new_book_infor.name_book_borrowed  = data['name_book_borrowed']
    new_book_infor.status = data['status']
    new_book_infor.remarks = data['remarks']
    #new_book_infor.duration = data['duration']
    new_book_infor.save()
    return json.dumps({'code':200,
                        "msg": "Book information arleady recorded"})

#vitendo vya mwanafunzi kuja kuchukua kitabu vimeishia apa

#vitendo vya mwanafunzi kurudisha kitabu vinaanza apo chini

def search_book_borrrowed(data):
  student = Student.students.get(registration_number=data["registration_number"])
  book_borrowed = Loan_book.loan_books.filter(student_id=student.student_id)
  serializers_book_borrowed = Loan_booktSerializer(book_borrowed, many=True).data
  
  return json.dumps({'code': 200, "name": serializers_book_borrowed})

def comment_book_borrowed(data):
  if Loan_book.loan_books.filter(nam_book_borrowed_id=data['nam_book_borrowed_id']).exists():

    book_taken = Loan_book.loan_books.get(nam_book_borrowed_id=data['nam_book_borrowed_id'])
    book_taken.remarks = data['remarks']
    book_taken.save()
    return  json.dumps({'code': 200,
                        "msg":"comment is succefully stored"})
  else:
        return json.dumps({'code': 300,
                       "msg": "Invalid book_comment"})