from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # s= "<h1>Welcome to my home!!!</h1>"
    # return HttpResponse(s)
    chats = ChatRoom.objects.all()
    context = {"chats": chats}
    return render(request, 'base.html', context)