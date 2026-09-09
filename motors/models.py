from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()





class Motor(models.Model):
    
    class CarType(models.TextChoices):
        CAR = 'Car', 'car'
        BUS = 'Bus', 'bus'
        MOTORBIKE = 'Motorbike', 'motorbike',
        BIKE = 'Bike', 'bike',
        
    owner  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='motors')
    car_type = models.CharField(choices=CarType.choices, default=CarType.CAR)
    RegNo = models.CharField(max_length=15, unique=True) 
    
    def __str__(self):
        return f"{self.RegNo}"   
