# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from qwiz.models import Question, Qwiz

def home_page(request):
	return render(request, 'home.html')

def view_qwiz(request, qwid_id):
	qwiz = Qwiz.objects.get(id=qwid_id)
	return render(request, 'qwiz.html', {'qwiz': qwiz})

def new_qwiz(request):
	qwiz = Qwiz.objects.create()
	Question.objects.create(text=request.POST['question_text'], qwiz=qwiz)
	return redirect('/qwiz/%d/' % (qwiz.id,))

def add_question(request, qwiz_id):
	qwiz = Qwiz.objects.get(id=qwiz_id)
	Question.objects.create(text=request.POST['question_text'], qwiz=qwiz)
	return redirect('/qwiz/%d/' % (qwiz.id,))
