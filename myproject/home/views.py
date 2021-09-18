from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import json
from  home.query import Librarian_registration
from  home.query import Librarian_login
from  home.query import student_registration
from  home.query import search_student_name
from  home.query import borrow_book
from  home.query import search_book_borrrowed
from  home.query import comment_book_borrowed


@csrf_exempt
def API(request):
    if request.method == "POST":
        client_request = request.body
        client_data = json.loads(client_request) 

    if client_data['code'] == 200:
         responseString = Librarian_registration(client_data['data'])

    if client_data['code'] == 201:
        responseString = Librarian_login(client_data['data'])

    if client_data['code'] == 202:
        responseString = student_registration(client_data['data'])
           
    if client_data['code'] == 203:
        responseString = search_student_name(client_data['data'])

    if client_data['code'] == 204:
        responseString = borrow_book(client_data['data'])

    if client_data['code'] == 205:
        responseString =  search_book_borrrowed(client_data['data'])

    if client_data['code'] == 206:
        responseString = comment_book_borrowed(client_data['data'])    

    return HttpResponse(responseString)  







