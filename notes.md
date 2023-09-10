# Django Learning

Using **pipenv** 

pip3 install pipenv 

pipenv install django

pipenv shell //start python interpreter inside the virtual env

```django-admin startproject storefront .```  (in current directory)

**manage.py**

Take configuration into consideration
```
python manage.py runserver [port=8000]
```


**settings.py**

*installed_apps* contain all apps to support django to work
```
python manage.py startapp playground
```



**template/hello.html**
This creates the front end to render to user, but not very common


Do not create apps that are monolithic or low coupling
**models.py**

Define all the models there



**Generic Object**
```
//For reading the object type  
content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
//for referencing the particular object
object_id = models.PositiveIntegerField() #limitation can only use id as primary key
//content_object for reading an actual object
content_object = GenericForeignKey()
```



**DATA Migration**
python3 manage.py makemigrations

Note: Use F2 to rename all instances
Trick: Use Command + T to find class or function definitions

If you change the migration file, be sure to change the depency file as well

Warning to add default

Option 1: Add one-off

Option 2: Add an app in models.py
1. Add null=**True**
2. default='something'

**Now how to run the migration**
```
python manage.py migrate
python manage.py sqlmigrate store 0003 //this will show actual sql code for migration
```

***How to properly remove the last migration***

```
python manage.py migrate store 0004 (assume we have 0005)

remove the 0005 mgiration file and related code chagnes in the code
```


***Do Mysql***
To work with MacOs(self research)

brew install mysql pkg-config
pip install mysqlclient

Command + Shift + O: to see synmbols in vscode, can be variable, functions,classes, etc


**Using empty migration**
```
python manage.py makemigrations store --empty
```


**Object Relational Mapping**

Reduce complexity in code, but  sql code is still needed when dealing with complicated query.

Migrations are part of django's RM

- model.objects 
  - returns a *manager* object, which is an interface to the database
  - model.objects.all() for example returns a *query set*  , which is an object encapsulates a query
  - query set is lazy, evaluated at a later time
  - We can use query set to build complex query
  
```
for product in query_set:
  print(product)
list(query_set)
query_set[0:5]
query_set.filter().filter().orderby()
```



