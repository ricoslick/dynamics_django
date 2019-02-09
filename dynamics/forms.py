"""
from django import forms

class UserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'title': 'Your name', 'id': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}), label='')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'title': 'Email Address', 'id': 'email', 'placeholder': 'Enter Email Address', 'class': 'form-group'}), label='')
	position = forms.CharField(widget=forms.TextInput(attrs={'title': 'Official rank', 'id': 'rank', 'placeholder': 'Enter Position', 'class': 'form-group'}), label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Your Password', 'id': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}), label='')
	password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Re-enter Password', 'id': 'cpassword', 'placeholder': 'Confirm Password', 'class': 'form-group'}), label='')
"""
from django.db import models
from django import forms
from django.forms import ModelForm
from .models import User

# UserForm for User objects
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'position', 'password', 'password_confirm']
		widgets = {
			'username': forms.TextInput(attrs={'title': 'Your Name', 'name': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}),
			'email': forms.EmailInput(attrs={'title': 'Your Email Address', 'name': 'email', 'placeholder': 'Enter Email', 'class': 'form-group'}),
			'position': forms.TextInput(attrs={'title': 'Official Rank', 'name': 'position', 'placeholder': 'Enter Rank', 'class': 'form-group'}),
			'password': forms.PasswordInput(attrs={'title': 'Your Password', 'name': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}),
			'password_confirm': forms.PasswordInput(attrs={'title': 'Re-enter Password', 'name': 'password_confirm', 'placeholder': 'Confirm Password', 'class': 'form-group'}),
		}
		labels = { 
			'username': '',
			'email': '',
			'position': '',
			'password': '',
			'password_confirm': '',
		 }

	def clean(self):
		 	cleaned_data = super(UserForm, self).clean()
		 	password = cleaned_data.get('password')
		 	password_confirm = cleaned_data.get('password_confirm')

		 	if password and password_confirm:
		 		if password != password_confirm:
		 			raise forms.ValidationError("Password fields must match.")

		 	return cleaned_data	 
		 


