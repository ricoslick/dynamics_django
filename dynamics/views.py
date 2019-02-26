from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login as customlogin

from .models import CustomUser
from .forms import RegisterationForm, CustomAuthForm
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'dynamics/index.html'

	def get_queryset(self):
		return CustomUser.objects.all()

class DashView(generic.DetailView):
	model = CustomUser
	slug_field = 'slug'
	template_name = 'dynamics/dashboard.html'

class LoginView(generic.DetailView):
	model = CustomUser
	authentication_form = 'CustomAuthenticationForm'


def register(request):
	# if POST request is made we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RegisterationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user.password = make_password(user.password)
			# user.password_confirm = make_password(user.password_confirm)
			user.save()
			messages.success(request, 'User account created successfully')
			success_url = reverse_lazy('login')
			return redirect(success_url)
		"""
		process the data in form.cleaned_date as required
		...
		redirect to a new URL:
		"""
	else:

		form = RegisterationForm()

	return render(request, 'dynamics/register.html', {
		'form':form
		})

def thanks(request, id):
	registered = get_object_or_404(CustomUser, pk=id)

	return render(request, 'dynamics/thanks.html', {'registered':registered})

def login(request):
	if request.method == 'POST':
		form = CustomAuthForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				customlogin(request, user)
				return redirect('index')
	else:

		form = CustomAuthForm()

	return render(request, 'dynamics/index.html', {
		'form':form
		})

# Custom Error Views
def customhandler404(request, exception, template_name='404.html'):
	response = render(request, '404.html')
	response.status_code = 404
	return response