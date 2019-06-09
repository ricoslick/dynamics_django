==========
Dynamics 
==========

Dynamics is a django-based web application for keeping track of member contributions in an investment group. 
Detailed documentation is in the 'docs' directory.

Quick Start
-------------

1. Add 'dynamics' into your settings.py file INSTALLED_APPS section like this:
	
	INSTALLED APPS= [
		...
		'dynamics',
	]

2. Include the dynamics URLconf in your project urls.py file like this:

	path('dynamics/', include('dynamics.urls')),

3. Run 'python manage.py migrate' to create the dynamics models.

4. Start the development server: 'python manage.py runserver', then visit 
'localhost:8000/dynamics' to begin interacting with the application.

5. To create a user account visit the 'Sign Up' page by clicking the 'Home' then 'Sign Up' buttons on the menu on the homepage('localhost:8000/dynamics'). This should redirect you to 'localhost:8000/register' page. Enter the requested information and await a confirmation email with further instructions.

6. Check your email for an 'account activation request', activate your account by clicking on the link provided in the email. This fails if have not setup a 'mailer' configuration in your settings.py file first. How to do that is beyond the scope of this document.

7. Proceed to the login page by visiting the link 'localhost:8000/login'.

8. To add a contribution for a member visit 'localhost:8000/dynamics/contribution' by clicking on 'Records' then 'Contributions' on the main menu ribbon.

9. Add your contribution by entering the 'Amount', selecting 'Contribution Date' and 'member' by default it should be the logged in member (you).
