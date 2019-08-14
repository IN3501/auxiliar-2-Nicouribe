from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miappaux2/index.html')

def pestaña (request):
	return render(request, 'miappaux2/pestaña.html')

def equipodocente (request):
	return render(request, 'miappaux2/equipodocente.html')

def aeleccion (request):
	return render(request, 'miappaux2/aeleccion.html')
	