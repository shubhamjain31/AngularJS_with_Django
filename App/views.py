from django.shortcuts import render, redirect
from .models import Employee

from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

def employee_list(request):
	return render(request, "employee_list.html")

@csrf_exempt
def employee_add(request):
	if request.method == "POST":
		data 	= json.loads(request.body)
		print(data)
		# username = data.get('username')


	return render(request, "employee.html")

def employee_edit(request):
	return render(request, "employee_list.html")

def employee_delete(request):
	return render(request, "employee_list.html")