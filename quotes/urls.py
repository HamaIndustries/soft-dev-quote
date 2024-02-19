"""
notes:
- python 3.12
- node.js LTS (20.11.1 LTS)
- python -m pip install -r requirements.txt
- cd frontend && npm install

to start the django server backend:
`python -m manage.py runserver`

to start javascript frontend:
`npm run dev`

to clean javascript (please do before committing)
`npm run format`


"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
]
