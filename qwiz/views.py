# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from qwiz.models import Question

def home_page(request):
	if request.method == 'POST':
		Question.objects.create(text=request.POST['question_text'])
		return redirect('/')
	
	questions = Question.objects.all()
	return render(request, 'home.html', {'questions': questions})