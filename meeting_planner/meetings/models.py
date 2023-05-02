from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):
    rname = models.CharField(max_length =200)
    flour_number =models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.rname} room {self.flour_number} on flour {self.room_number}"
    
    
    
class Meeting(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateField()
    start_time =models.TimeField(default=time(7))
    duration =models.IntegerField(default=1)
    room =models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


