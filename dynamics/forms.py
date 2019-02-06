from django import forms

class UserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'title': 'Your name', 'id': 'username', 'placeholder': 'Enter Username', 'class': 'form-group'}), label='')
	email = forms.EmailField(widget=forms.EmailInput(attrs={'title': 'Email Address', 'id': 'email', 'placeholder': 'Enter Email Address', 'class': 'form-group'}), label='')
	position = forms.CharField(widget=forms.TextInput(attrs={'title': 'Official rank', 'id': 'rank', 'placeholder': 'Enter Position', 'class': 'form-group'}), label='')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Your Password', 'id': 'password', 'placeholder': 'Enter Password', 'class': 'form-group'}), label='')
	password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'title': 'Re-enter Password', 'id': 'cpassword', 'placeholder': 'Confirm Password', 'class': 'form-group'}), label='')

