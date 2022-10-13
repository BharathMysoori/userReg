from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from .models import Customer
import os
from django.http import HttpResponse
from django.contrib import messages
# Create your views here. 
@user_passes_test(lambda user: not user.username, login_url='/', redirect_field_name=None)
def registerView(request):
	if request.method == 'POST':
		uname = request.POST.get('username')
		upass = request.POST.get('userpass')
		cpass = request.POST.get('userpass1')
		ugender = request.POST.get('gender')
		umail = request.POST.get('useremail')
		category  = request.POST.get('usercat')
		contact = request.POST.get('usercontact')
		avatar = request.FILES.get('avatar')
		
		if upass == cpass:
			
			if User.objects.filter(username=uname).exists():
				messages.info(request,'Username already taken')
				print("username")
				return render(request,'registerTest.html')
			elif User.objects.filter(email=umail).exists():
				messages.info(request,'Email already taken')
				print('mail')
				return render(request,'registerTest.html')

				
			
			else:

				newuser = User.objects.create_user(username=uname,email=umail,password=upass)
				
				print(newuser,category,contact)
				print("user saved")
				newuser.save()
				
				newuser.customer.category = category
				newuser.customer.contactNo = contact
				newuser.customer.userpic = avatar
				newuser.save()

				
				print("Customer added")
				messages.success(request, 'Registration successfull')
				
				return redirect('loginpage')
		else:
			messages.error(request,'Both passwords doest match')
			return render('registerTest.html')
			
		

		
			
			
			
			
		
		
	else:
		return render(request,'registerTest.html')
@user_passes_test(lambda user: not user.username, login_url='/', redirect_field_name=None)
def loginView(request):
	if request.method == 'POST':
		uname = request.POST['username']
		upass = request.POST['userpass']
		
		user = authenticate(request,username=uname,password=upass)
		
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.error(request,'Username and Password Doesnt match Try again')
			return render(request,'login.html')
			#return HttpResponse('login failed')
	else:
		return render(request,'login.html')
def logoutView(request):
	logout(request)
	return redirect('loginpage')
@login_required(login_url='login/')
def homeView(request):
	data = Customer.objects.filter(user=request.user)
	return render(request,'home.html',{'data':data})


@login_required(login_url='login/')
def viewprofile(request):
	profile_data = Customer.objects.filter(user=request.user)
	if request.method == 'POST':
		fname = request.POST.get('fname')
		surname = request.POST.get('surname')
		contact = request.POST.get('contact')
		mailid = request.POST.get('mailid')
		category = request.POST.get('category')
		for d in profile_data:
				d.firstName = fname
				d.surname= surname
				d.contactNo = contact
				d.category = category
				d.user.email = mailid
				d.userpic = request.FILES.get('pic')
				d.save()
	return render(request,'viewprofile.html',{"data":profile_data})
		
		
def profileview(request):
	return render(request,'profile.html')		
	







def updateCustomer(request):
	data = Customer.objects.filter(user=request.user)
	#updata = Customer.objects.get(id=pk)
	print(data)
	#print(updata)
	if request.method == 'POST':
		fname = request.POST.get('fname')
		surname = request.POST.get('surname')
		contact = request.POST.get('contact')
		mailid = request.POST.get('mailid')
		category = request.POST.get('category')
		print(data,fname,surname,contact)
		for d in data:
			d.firstName = fname
			d.surname= surname
			d.contactNo = contact
			d.category = category
			d.user.email = mailid
			d.save()


		#print(updata)
	return render(request,'viewprofile.html',{'data':data})



















