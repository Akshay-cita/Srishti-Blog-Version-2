from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


@login_required
def home(request):
	post=Post.objects.all()
	profile=Profile.objects.all()
	context={'post':post,'profile':profile}
	return render(request,'app1/home.html',context)


class PostListView(ListView):
	model=Post
	template_name='app1/home.html'
	context_object_name='post'
	ordering=['-date_time']


class PostDetailView(DetailView):
	model=Post
	#template_name='app1/post_detail.html'


class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False  

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False  


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
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST, instance=request.user)
		p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance =request.user)
		p_form = ProfileUpdateForm(instance=request.user)
		
		
	context={'u_form':u_form,'p_form':p_form}
	return render(request,'app1/profile.html',context)

