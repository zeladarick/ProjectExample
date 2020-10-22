from django.http import HttpResponse
from django.shortcuts import render

def list_posts(request):
    return render(request, "index.html")
    #return HttpResponse("holaaa")
# Create your views here.
