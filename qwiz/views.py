# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from qwiz.models import Question

def home_page(request):
	if request.method == 'POST':
		Question.objects.create(text=request.POST['question_text'])
		return redirect('/qwiz/the-only-qwiz-in-the-world/')
	return render(request, 'home.html')

def view_qwiz(request):

	questions = Question.objects.all()
	return render(request, 'qwiz.html', {'questions': questions})

	

