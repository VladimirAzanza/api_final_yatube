# API YaTube

This is a work in progress of the API to YaTube.

YaTube is an application where users can interact with others through posts or comments to posts, and they can also follow their idols.

This package includes the RESTful API created with Django REST Framework. The idea is to have a simple API to proof concepts such as: serializers, viewsets, regular expresions, permissions, filtration and documentation.




## Installation

Install API YaTube with activated venv (Linux):

```bash
  python -m venv ./venv
  source .venv/bin/activate
```
next, install dependencies:
```bash
  pip install -r requirements.txt
```
migrate:
```bash
  python manage.py migrate
```
Finally, run the project with:
```bash
  python manage.py runserver
```

## Documentation

[Documentation ReDoc](https://http://127.0.0.1:8000/redoc/)


## 🛠 Skills
Python, Django, DRF, API RESTFul, Postman


## Running Collection at Postman

To run collections, go to postman_collection directory

(Attention - this command will clean the existing database):
```bash
  bash set_up_data.sh
```

Go back to manage.py directory and runserver:
At postman app:
```
    1. import CRUD_for_yatube.postman_collection.json 
    2. press button Run collection
    3. press button Run CRUD_for_yatube
```