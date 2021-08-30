from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Position

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse, HttpResponse

import uuid
import json
from validators import is_invalid
from django.core import serializers

# Create your views here.

def employee_list(request):
	all_employees = Employee.objects.values('username', 
											'fullname',
											'first_name',
											'last_name',
											'email',
											'emp_code',
											'mobile',
											'joining_date',
											'position__title',
											'id')

	params = {"all_employees":list(all_employees)}

	return render(request, "employee_list.html", params)

@csrf_exempt
def employee_add(request):
	if request.method == "POST":
		data 		= json.loads(request.body)

		username 	= data.get('username')
		firstname 	= data.get('first_name')
		lastname 	= data.get('last_name')
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
								username    = username,
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

	# obj = get_object_or_404(Employee, id = id)
	employee_data = Employee.objects.filter(id=id)
	
	obj = employee_data.values('username', 
								'fullname',
								'first_name',
								'last_name',
								'email',
								'emp_code',
								'mobile',
								'joining_date',
								'position__title',
								'id')

	if request.method == "POST":
		data 		= json.loads(request.body)

		username 	= data.get('username')
		firstname 	= data.get('first_name')
		lastname 	= data.get('last_name')
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

	params = {"obj":list(obj)}
	return render(request, "employee.html", params)

def employee_delete(request):
	return render(request, "employee_list.html")