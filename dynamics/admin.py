from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterationForm, CustomUserChangeForm
from .models import CustomUser, Contribution

# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = RegisterationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'email',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contribution)

