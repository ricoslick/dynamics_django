from django.urls import path

from . import views

app_name = 'dynamics'
urlpatterns = [
	# ex: /dynamics/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /dynamics/login
	path('<int:pk>/', views.DashView.as_view(), name='dashboard'),
	# ex: /dynamics/register
	path('register/', views.register, name='register'),
	# ex: /dynamics/url(username slug)
	path('<slug>/', views.thanks, name='thanks'),
]