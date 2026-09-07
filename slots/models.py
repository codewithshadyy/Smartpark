from django.db import models

class Slot(models.Model):
    
    class SlotSatus(models.TextChoices):
        VACANT = "vacant", 'vacant'
        BOOKED = "Booked", "booked"
        
    

    number = models.CharField(max_length=15)
    status = models.CharField(choices=SlotSatus, default=SlotSatus.VACANT) 
    
