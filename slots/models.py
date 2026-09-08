from django.db import models

class Slot(models.Model):
    
    class SlotSatus(models.TextChoices):
        VACANT = "vacant", 'vacant'
        BOOKED = "Booked", "booked"
        
    

    number = models.CharField(max_length=15, unique=True)
    status = models.CharField(choices=SlotSatus, default=SlotSatus.VACANT) 
    
    def __str__(self):
        return f"{self.number}"
