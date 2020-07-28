from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return render(request,'app1/home.html')
	
@login_required
def about(request):
	return render(request,'app1/about.html')


def register(request):
	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account is created for user {username}!!')
			return redirect('login')
	else:

		form=CreateUserForm()

	return render(request,'app1/register.html',{'form':form})

@login_required
def profile(request):
	return render(request,'app1/profile.html')

