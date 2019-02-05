from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import User, Investments, Contribution
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'dynamics/index.html'

	def get_queryset(self):
		return User.objects.all()


