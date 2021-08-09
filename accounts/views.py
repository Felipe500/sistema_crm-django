from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post,Contato
# Create your views here.
def inicio(request):
	return render(request, 'accounts/dashboard.html')

def prod(request):
	return render(request, 'accounts/produtos.html')

def cust(request):
	return render(request, 'accounts/customize.html')