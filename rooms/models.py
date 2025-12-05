from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()

    def __str__(self):
        return self.name

