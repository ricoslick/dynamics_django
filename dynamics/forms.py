from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.forms.widgets import PasswordInput, TextInput, DateInput
from datetime import date
# from bootstrap_datepicker_plus import DatePickerInput
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

# from django.forms import ModelForm
from .models import CustomUser, Contribution
# Override AuthenticationForm to customize login
class CustomAuthForm(AuthenticationForm):
	# customizing fields done here
	username = forms.CharField(widget=forms.TextInput(attrs={'title': 'Your name', 'id': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}), label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Your Password', 'id': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}), label='')

	class Meta:
		model = CustomUser
		fields = ['username', 'password']
		widgets = {
			'username':forms.TextInput(attrs={'title': 'Your Name', 'name': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}),
			'password':forms.PasswordInput(attrs={'title': 'Your Password', 'name': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}),
		}
		labels = {
			'username':'',
			'password':'',
		}


	def clean(self):
		cleaned_data = super(CustomAuthForm, self).clean()
		return cleaned_data
	# throw error if account not activated(via email)	
	def confirm_login_allowed(self, user):
		if not user.is_active:
			raise forms.ValidationError("Sorry, This account is inactive.", code='inactive')


# CustomUserForm for User objects
class RegisterationForm(UserCreationForm):
	password1 = forms.CharField(label= '', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-group','name': "password1",'type': "password", 'placeholder': 'Enter Password'}))
	password2 = forms.CharField(label= '', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-group','name': "password2",'type': "password", 'placeholder': 'Confirm Password'}))

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ['username', 'email', 'post']
		widgets = {
			'username': forms.TextInput(attrs={'title': 'Your Name', 'name': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}),
			'email': forms.EmailInput(attrs={'title': 'Your Email Address', 'name': 'email', 'placeholder': 'Enter Email', 'class': 'form-group'}),
			'post': forms.TextInput(attrs={'title': 'Official Rank', 'name': 'position', 'placeholder': 'Enter Rank', 'class': 'form-group'}),
			# 'password1': forms.PasswordInput(attrs={'title': 'Your Password', 'name': 'password1', 'placeholder': 'Enter Password', 'class': 'form-group'}),
			# 'password_confirm': forms.PasswordInput(attrs={'title': 'Re-enter Password', 'name': 'password_confirm', 'placeholder': 'Confirm Password', 'class': 'form-group'}),
		}
		labels = { 
			'username': '',
			'email': '',
			'post': '',
			# 'password1': '',
			# 'password_confirm': '',
		 }

	def clean(self):
		 	cleaned_data = super(RegisterationForm, self).clean()
		 	password = cleaned_data.get('password1')
		 	password_confirm = cleaned_data.get('password2')

		 	if password and password_confirm:
		 		if password != password_confirm:
		 			raise forms.ValidationError("Password fields must match.")

		 	return cleaned_data	 
		 
class CustomUserChangeForm(UserChangeForm):
	password1 = forms.CharField(label= '', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-group','name': "password1",'type': "password", 'placeholder': 'Enter Password'}))
	password2 = forms.CharField(label= '', max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-group','name': "password2",'type': "password", 'placeholder': 'Confirm Password'}))


	class Meta:
		model = CustomUser
		fields = ['username', 'email', 'post', 'password', 'password_confirm', 'is_active']
		widgets = {
			'username': forms.TextInput(attrs={'title': 'Your Name', 'name': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}),
			'email': forms.EmailInput(attrs={'title': 'Your Email Address', 'name': 'email', 'placeholder': 'Enter Email', 'class': 'form-group'}),
			'post': forms.TextInput(attrs={'title': 'Official Rank', 'name': 'position', 'placeholder': 'Enter Rank', 'class': 'form-group'}),
			# 'password': forms.PasswordInput(attrs={'title': 'Your Password', 'name': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}),
			# 'password_confirm': forms.PasswordInput(attrs={'title': 'Re-enter Password', 'name': 'password_confirm', 'placeholder': 'Confirm Password', 'class': 'form-group'}),
		}
		labels = { 
			'username': '',
			'email': '',
			'post': '',
			# 'password': '',
			# 'password_confirm': '',
		 }

	def clean_password(self):

		return self.initial["password1", "password2"]

		
class CustomSetPassForm(SetPasswordForm):
	new_password1 = forms.CharField(label= '', max_length=200, required=True, widget=forms.PasswordInput(attrs={'class': 'form-group','name': "new_password1",'type': "password", 'placeholder': 'Enter New Password'}))
	new_password2 = forms.CharField(label= '', max_length=200, required=True, widget=forms.PasswordInput(attrs={'class': 'form-group','name': "new_password2",'type': "password", 'placeholder': 'Confirm Password'}))

class CustomPassResetForm(PasswordResetForm):
	email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'title': 'Enter email address here', 'id': 'email', 'placeholder': 'Enter Email', 'class': 'form-group'}), label='')

# Model Form for Contribution model
class ContributionForm(forms.ModelForm):
	member = forms.ModelChoiceField(queryset=CustomUser.objects.all(), empty_label=("--Select Current User--"), widget=forms.Select(attrs={'class':'custom-select'}))
	class Meta:
		model = Contribution
		fields = ['amount', 'Contribution_date', 'member']
		widgets = {
			'amount': forms.NumberInput(attrs={'title': 'Enter Amount Given', 'name':'amount', 'placeholder': 'Enter Contribution', 'class': 'form-group'}), 
			'Contribution_date': forms.DateInput(attrs={'title': 'Pick Date of Contribution', 'name': 'contribution_date', 'placeholder': 'Select Date', 'class':'form-group', 'data-provide': 'datepicker', 'id': 'contribution_date'}),
		}	
		labels = {
			'amount': '',
			'Contribution_date': '',
			'member': ''
		}

	# validate Contribution_date and choicefield option:
	def clean(self):
		 	cleaned_data = super(ContributionForm, self).clean()
		 	member = cleaned_data.get('member')
		 	Contribution_date = cleaned_data.get('Contribution_date')

		 	if Contribution_date > date.today():
		 		raise forms.ValidationError("Invalid date! Contribution cannot be added in the future")


		 	return cleaned_data	


	


