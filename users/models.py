from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
        class Role(models.TextChoices):
            ADMIN = 'Admin', 'administrator'
            ATTENDANT='Attend', 'attendant'
            DRIVER = 'Driver', 'driver'
            
        role = models.CharField(choices=Role.choices, default=Role.DRIVER, max_length=200)
        email = models.EmailField(unique=True)
        is_verified = models.BooleanField(default=False)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username'] 
        
        def __str__(self):
              return f"{self.email}"    
