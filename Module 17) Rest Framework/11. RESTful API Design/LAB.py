Step 1: Create a New Django Project and App
Create a new Django project and an app for managing doctor records.

bash
Copy
Edit
django-admin startproject doctor_management
cd doctor_management
python manage.py startapp doctors
Step 2: Set Up the Database (SQLite by Default)
1. Configure SQLite (Default Database)

By default, Django uses SQLite, which requires no additional setup. Just check the DATABASES setting in the doctor_management/settings.py file:

python
Copy
Edit
# doctor_management/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Using SQLite by default
        'NAME': BASE_DIR / 'db.sqlite3',         # Database file
    }
}
If you're using SQLite, no further changes are necessary, and you can proceed with the database setup.

2. Configuring MySQL (Optional)

If you prefer to use MySQL, you need to install the MySQL client for Python:

bash
Copy
Edit
pip install mysqlclient
Then, modify the DATABASES setting to use MySQL:

python
Copy
Edit
# doctor_management/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Using MySQL
        'NAME': 'doctor_db',                   # Database name
        'USER': 'root',                        # Your MySQL username
        'PASSWORD': 'yourpassword',            # Your MySQL password
        'HOST': 'localhost',                   # Typically 'localhost'
        'PORT': '3306',                        # Default MySQL port
    }
}
Make sure you’ve created the database (doctor_db in this example) in MySQL:

sql
Copy
Edit
CREATE DATABASE doctor_db;
Step 3: Create the Doctor Model
In the models.py file of the doctors app, create a model to store doctor records.

python
Copy
Edit
# doctors/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"
Explanation:

name: Name of the doctor.

specialty: The medical specialty (e.g., cardiologist, dermatologist).

phone_number: Contact number of the doctor.

email: Doctor's email.

address: Office or practice address.

Step 4: Make Migrations and Migrate the Database
After creating the model, run the migrations to create the corresponding table in the database.

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
This will generate the necessary database schema and create the table for the Doctor model.

Step 5: Create an Admin Interface to Manage Doctor Records
Django provides an admin interface to manage data easily. To enable this:

Register the Doctor model in admin.py:

python
Copy
Edit
# doctors/admin.py

from django.contrib import admin
from .models import Doctor

admin.site.register(Doctor)
Create a superuser to access the admin panel:

bash
Copy
Edit
python manage.py createsuperuser
After creating the superuser, run the server:

bash
Copy
Edit
python manage.py runserver
Now, you can access the Django admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials to manage doctor records.

Step 6: Add Views to Display Doctor Records (Optional)
To display doctor records on a webpage, create a view in views.py and a corresponding template.

python
Copy
Edit
# doctors/views.py

from django.shortcuts import render
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()  # Get all doctor records
    return render(request, 'doctor_list.html', {'doctors': doctors})
Create a template for displaying the doctor records:

html
Copy
Edit
<!-- doctors/templates/doctor_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Doctor List</title>
</head>
<body>
    <h1>List of Doctors</h1>
    <ul>
        {% for doctor in doctors %}
            <li>{{ doctor.name }} - {{ doctor.specialty }}</li>
        {% endfor %}
    </ul>
</body>
</html>
Update urls.py to add a URL pattern for the doctor list view:

python
Copy
Edit
# doctors/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
]
Step 7: Run the Server and Test the Application
After completing the above steps, run the server:

bash
Copy
Edit
python manage.py runserver
Now, visit http://127.0.0.1:8000/ to see the list of doctors (if you have added records via the Django admin interface).

