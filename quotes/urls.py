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
from django.urls import path, include

from . import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/quote/history', api.quote_history_api),
    path('api/quote/form', api.quote_form_api),
    path('api/login', include("login.urls")),
    path('api/profile_mgmt', include("profile_mgmt.urls")),
    path('api/pricing/', include("pricing.urls"))
]
