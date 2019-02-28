from django.urls import path, re_path
from django.contrib.auth import views as auth_views 

from . import views
from .forms import CustomAuthForm, CustomPassResetForm, CustomSetPassForm

app_name = 'dynamics'
urlpatterns = [
	# ex: /dynamics/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /dynamics/dashboard
	path('users/<slug:slug>/', views.DashView.as_view(), name='dashboard'),
	path('contribution/', views.contribution, name='contribution'),
	# ex: /dynamics/register
	path('register/', views.register, name='register'),
	# ex: /dynamics/register/thanks
	path('register/thanks/', views.thanks, name='thanks'),
	# ex: /dynamics/login
	path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthForm), name='login'),
	# ex: /dynamics/password_reset
	path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPassResetForm), name='password_reset'),
	# ex: /dynamics/password_reset_done
	path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	# ex: /dynamics/password_reset_confirm
	path('password_reset_confirm', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPassForm), name='password_reset_confirm'),
	# ex: /dynamics/password_reset_complete
	path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
