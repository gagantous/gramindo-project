from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "book/index.html",
    	{'title': 'DAFTAR BUKU'})
# Create your views here.
