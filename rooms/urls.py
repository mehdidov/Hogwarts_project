from django.urls import path
from . import views

urlpatterns = [
    # URL that will display the list of rooms
    path("", views.list_room, name="list_room"),


]