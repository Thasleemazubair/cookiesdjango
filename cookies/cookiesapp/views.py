from django.http import HttpResponse
from django.shortcuts import render


def set_cookie(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('user_id','12345',max_age=3600)
    return response

def get_cookie(request):
    user_id = request,COOKIES.get('user_id','No cookies set')
    return HttpResponse("Cookie.value:{ user_id }")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('user_id')
    return response