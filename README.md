
># Status : Developing ⚠️

## Adding Bootstrap forms in templates
+ Product
+ Client
+ Technician
+ Services

> member staff and superuser can add and edit forms in templates

## Adding UUID on all Models
for the generate random ID fields


## Technologies Used
<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>Docker</td>
    <td>Docker-compose</td>
  </tr>
</table>

## How to run Application:
1) clone this repository
2) pip install requirements.txt
3) change line 87 in settings.py for 'default' and line 91 for 'postgres'
4) python manage.py makemigrations accounts
5) python manage.py migrate
6) python manage.py createsuperuser
7) python manage.py runserver
8) Enjoy! 😃

# Adding Docker on Project

## How to run Application with Docker:
1) clone this repository
2) run in command line ***docker-compose --build*** 
3) docker-compose up -d
4) docker-compose logs ***for exhibition of logs***
5) docker-compose exec web python manage.py makemigrations accounts 
6) docker-compose exec web python manage.py migrate
7) docker-compose exec web python manage.py createsuperuser
8) docker-compose exec web python manage.py runserver 
9) Enjoy! 😃
