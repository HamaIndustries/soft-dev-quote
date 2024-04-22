from django.urls import path

from . import views

app_name = "login"
urlpatterns = [
    # examples
    # path("", views.IndexView.as_view(), name="index"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("", views.current_datetime, name="curent_datetime"),
    path("", views.login_api, name="login_api"),
    path("register", views.registerAccount, name="login_api")
]