# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):

	return render(request, 'home.html',
		{'new_item_text': request.POST.get('item_text','')}
		)
	