from django.db import models
from rooms.models import Room

# Create your models here.
Hogwarts_House = [
    ("Gryffindor","Gryffindor"),
    ("Slytherin","Slytherin"),
    ("Ravenclaw,","Hufflepuff"),
    ("Hufflepuff","Hufflepuff"),
]

class Bookings(models.Model):


    def __str__(self):
        return 
