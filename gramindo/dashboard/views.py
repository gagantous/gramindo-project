from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "dashboard/index.html",
    	{'title': 'HALAMAN DEPAN'})
# Create your views here.
