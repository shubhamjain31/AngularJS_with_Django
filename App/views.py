from django.shortcuts import render, redirect
from .models import Employee, Position

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse

import uuid
import json
from validators import is_invalid

# Create your views here.

def employee_list(request):
	employee_obj = Employee.objects.all()

	return render(request, "employee_list.html", {"all_employees":employee_obj})

@csrf_exempt
def employee_add(request):
	last = request.META.get('HTTP_REFERER', None)

	if request.method == "POST":
		data 		= json.loads(request.body)

		username 	= data.get('username')
		firstname 	= data.get('firstname')
		lastname 	= data.get('lastname')
		email 		= data.get('email')
		mobile 		= data.get('mobile')
		position 	= data.get('position')

		if username is None:
			msg = "Please Enter Username !"
			return JsonResponse({'error':True, 'msg':msg})

		if firstname is None:
			msg = "Please Enter Firstname !"
			return JsonResponse({'error':True, 'msg':msg})

		if lastname is None:
			msg = "Please Enter Lastname !"
			return JsonResponse({'error':True, 'msg':msg})

		if email is None:
			msg = "Please Enter Email !"
			return JsonResponse({'error':True, 'msg':msg})

		if position is None:
			msg = "Please Enter Position !"
			return JsonResponse({'error':True, 'msg':msg})

		fname = firstname.capitalize()
		lname = lastname.capitalize()

		position_obj = Position.objects.create(title=position.capitalize())

		Employee.objects.create(
								fullname 	= fname + ' ' + lname,
								first_name  = fname,
								last_name 	= lname,
								email 		= email,
								emp_code 	= uuid.uuid4(),
								mobile 		= mobile,
								position 	= position_obj
							)

		msg = "Employee Added !"
		return JsonResponse({'saved':True, 'msg':msg})

	return render(request, "employee.html")

def employee_edit(request, id):
	return render(request, "employee.html")

def employee_delete(request):
	return render(request, "employee_list.html")