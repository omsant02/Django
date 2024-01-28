from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    peoples =[
        {'name':'rohan', 'age':26},
        {'name':'sumit', 'age':20},
        {'name':'alpha', 'age':16}
    ]
     
    return render(request, "home/index.html", context = {'peoples':peoples, "page":"Django"})

def about(request):
    context = {"page" : "About"}
    return render(request, "home/about.html",  context)

def contact(request):
    context = {"page" : "Contact"}
    return render(request, "home/contact.html",  context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a Success page</h1>")