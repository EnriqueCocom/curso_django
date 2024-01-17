from django.db import models

# Create your models here.

class Usuarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null = False)
    lastname = models.CharField(max_length=20, null = False)
    telefono = models.CharField(max_length=10, null = True, blank = True)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
