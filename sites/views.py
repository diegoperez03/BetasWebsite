from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
	return render(request,'main.html')
def snap(request):
	return render(request,'snap.html')
def home(request):
	return render(request,'home.html')
def actives(request):
	return render(request,'actives.html')
def events(request):
	return render(request, 'events.html')
def strolling(request):
	return render(request, 'strolling.html')
def recruitment(request):
	return render(request, 'recruitment.html')

def history(request):
	return render(request, 'history.html')