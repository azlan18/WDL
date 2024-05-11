For any Django projects:
Create project directory

    mkdir dir
    cd dir

Create Virtual env:
    
    python -m venv myenv

Activate virtual env:

    .\myenv\scripts\activate

Now install django

    pip install django
    pip list #to check if installed
------------------------------------------------------------------------------------------------------------------------
Start project #Ignore if cloning project
    
    django-admin startproject proj_name
    cd proj_name
    python manage.py startapp myapp #create your views, templates, urls, models here
------------------------------------------------------------------------------------------------------------------------
 After making any changes to a model run:

    python manage.py makemigrations
    python manage.py migrate
