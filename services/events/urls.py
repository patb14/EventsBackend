from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("ajax/load_times/", views.event_times_view, name="ajax_load_times"),
]