from django.urls import path

from . import views

app_name = "profile_mgmt"
urlpatterns = [
     #path("", views.current_datetime ,name="current_datetime"),
    path("", views.profile_mgmt_api, name="profile_api"),
    # examples
    # path("", views.IndexView.as_view(), name="index"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]