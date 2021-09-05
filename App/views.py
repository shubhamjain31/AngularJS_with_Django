from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Position

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

import uuid
import json
from validators import is_invalid

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
		position 	= data.get('position__title')

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

		position_obj = Position.objects.create(title=position.title())

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

@csrf_exempt
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

	if request.method == "PUT":
		data 		= json.loads(request.body)

		username 	= data.get('username')
		first_name 	= data.get('first_name')
		last_name 	= data.get('last_name')
		email 		= data.get('email')
		mobile 		= data.get('mobile')
		position 	= data.get('position__title')

		if username is None:
			msg = "Please Enter Username !"
			return JsonResponse({'error':True, 'msg':msg})

		if first_name is None:
			msg = "Please Enter Firstname !"
			return JsonResponse({'error':True, 'msg':msg})

		if last_name is None:
			msg = "Please Enter Lastname !"
			return JsonResponse({'error':True, 'msg':msg})

		if email is None:
			msg = "Please Enter Email !"
			return JsonResponse({'error':True, 'msg':msg})

		if position is None:
			msg = "Please Enter Position !"
			return JsonResponse({'error':True, 'msg':msg})

		fname = first_name.capitalize()
		lname = last_name.capitalize()

		update_obj = employee_data.first()

		Employee.objects.filter(id=id).update(username 	= username,
											fullname 	= fname + ' ' + lname,
											first_name 	= fname,
											last_name 	= lname,
											email 		= email,
											mobile 		= mobile
											)

		Position.objects.filter(pk=update_obj.position.id).update(title=position.title())

		msg = "Employee Updated !"
		return JsonResponse({'saved':True, 'msg':msg})

	params = {"obj":list(obj)}
	return render(request, "employee.html", params)

@csrf_exempt
def employee_delete(request, id):
	if id != 0:
		obj = Employee.objects.get(id=id)
		obj.delete()
		messages.success(request, 'Employee Deleted !')
		return redirect('/')

	if request.method == "DELETE":
		data 		= json.loads(request.body)

		id_ 	= data.get('id')
		obj = Employee.objects.get(id=id_)
		obj.delete()

		msg = "Employee Deleted !"
		return JsonResponse({'deleted':True, 'msg':msg})

	return render(request, "employee_list.html")

@csrf_exempt
def search(request):
	if request.method == "POST":
		search 		= request.POST.get('search')

		obj = Employee.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))

	return render(request, "search.html", {'obj':obj})