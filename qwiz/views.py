# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from qwiz.models import Question, Qwiz

def home_page(request):
	return render(request, 'home.html')

def view_qwiz(request):
	questions = Question.objects.all()
	return render(request, 'qwiz.html', {'questions': questions})

def new_qwiz(request):
	qwiz = Qwiz.objects.create()
	Question.objects.create(text=request.POST['question_text'], qwiz=qwiz)
	return redirect('/qwiz/the-only-qwiz-in-the-world/')

