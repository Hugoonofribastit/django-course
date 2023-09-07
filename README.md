Comenzamos instalando el virtualenv y ejecutandolo
pip install virtualenv 
virtualenv venv  
.\venv\Scripts\activate

instalamos django
pip install django

creo el proyecto que contendra mi app de la siguiente manera
django-admin startproject mysite .

paso a crear mi app con 
python manage.py startapp myapp

luego ya puedo ejecutar el 
python manage.py runserver

cuando creo los modelos en myapp los migro con los siguientes comandos
manage.py makemigrations myapp
manage.py migrate myapp

puedo agregar tablas con shell
"python manage.py shell"
from myapp.models import Project, Task
p = Project(name="aplicacion movil")
p.save()                     	 para que la guarde en la DB
Project.objects.all() 		 trae los obj de la db
Project.objects.get(id=1)

para la seccion de tasks

from myapp.models import Project, Task
p = Project.objects.get(id=1)
p.save()
p.task_set.all()

Project.objects.filter(name__startswith="aplicacion") 


PARA LA SECCION DE ADMIN DE DJANGO:
manage.py createsuperuser
* AHI SETEO EL USER Y LA PASSWORD
* entro al localhost:3000/admin por ejemplo y ahi ya puedo logear y usar el panel, conectado a mi base de datos predeterminada(sqlite) o seteada. 
