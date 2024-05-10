from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.

#This is where we render our html templates with dynamic blocks
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})