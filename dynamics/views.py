from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.hashers import make_password

from .models import User, Investments, Contribution
from .forms import UserForm
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'dynamics/index.html'

	def get_queryset(self):
		return User.objects.all()

class DashView(generic.DetailView):
	model = User
	slug_field = 'url'
	template_name = 'dynamics/dashboard.html'
	
def register(request):
	# if POST request is made we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.password = make_password(user.password)
			user.password_confirm = make_password(user.password_confirm)
			user.save()
			return HttpResponseRedirect('dynamics/thanks')
		"""
		process the data in form.cleaned_date as required
		...
		redirect to a new URL:
		"""
	else:

		form = UserForm()

	return render(request, 'dynamics/register.html', {
		'form':form
		})

def thanks(request, slug):
	get_object_or_404(User, slug)