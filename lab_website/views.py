from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
	return render(request, 'home.html')

def people(request):
	return render(request, 'people.html')

def docs(request):
	return render(request, 'docs.html')

def gallery(request):
	return render(request, 'gallery.html')

def links(request):
	return render(request, 'links.html')

def access(request):
	return render(request, 'access.html')
