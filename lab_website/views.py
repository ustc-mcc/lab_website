from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
	return render(request, 'home.html')

def people(request):
	return render(request, 'people.html')

def docs(request):
	return render(request, 'docs.html')

def gallery(request, page=None):
	if page:
		return render(request, 'gallery_'+str(page)+'.html')
	return render(request, 'gallery.html')

def publications(request):
	return render(request, 'publications.html')

def access(request):
	return render(request, 'access.html')
