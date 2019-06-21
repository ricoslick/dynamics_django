from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login as customlogin
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch 
from datetime import date
from bootstrap_datepicker_plus import DatePickerInput
from io import BytesIO

from .models import CustomUser, Contribution
from .forms import RegisterationForm, CustomAuthForm, ContributionForm
from .pdf_utils import PdfPrint
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

@login_required(login_url='login')
def thanks(request):
	contribution_list = Contribution.objects.all().select_related().order_by('-Contribution_date')
	template_name = 'dynamics/thanks.html'
	return render(request, template_name, {'contribution_list': contribution_list})

	

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
# Contributions view: user redirected to login page if attempting to access page without signing in
@login_required(login_url='login')
def contribution(request):
	if request.method == 'POST':
		# member = CustomUser.objects.get(pk=request.user.id)
		form_contrib = ContributionForm(request.POST)
		if form_contrib.is_valid():
			contribution = form_contrib.save()
			contribution.save()
			messages.success(request, 'Contribution added') 
			success_url = reverse_lazy('dynamics:thanks')
			return redirect(success_url)
		else:
			messages.error(request, 'Contribution not added')
	else:
		form_contrib = ContributionForm()

	return render(request, 'dynamics/dashboard.html', {'form_contrib': form_contrib})


# Downloads Pdf View: user downloads a pdf document
@login_required(login_url='login')
def pdfdownload(request):
	contribution_list = Contribution.objects.all().select_related().order_by('-Contribution_date')
	member = None
	if request.method == 'POST':
		form = ContributionForm(request.POST)
		if form.is_valid():
			member_id = form.data['member']
			member = CustomUser.objects.get(pk=member_id)
			contribution_list = Contribution.objects.filter(member=member_id)
		if 'pdf' in request.POST:
			response = HttpResponse(content_type='application/pdf')
			today = date.today()
			filename = 'contribution_report' + today.strftime('%Y-%m-%d')
			response['Content-Disposition'] = 'attachment; filename={0}.pdf'.format(filename)
			buffer = BytesIO()
			report = PdfPrint(buffer, 'A4')
			pdf = report.report(contribution_list, 'Contribution List info')
			response.write(pdf)
			return response
	else:
		form = ContributionForm()

	template_name = 'dynamics/download.html'
	context = {
		'form': form,
		'member': member,
		'contribution_list': contribution_list,
	}
	return render(request, template_name, context)



