from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

class Planning(models.Model):
     name = models.TextField()
     desc = models.TextField()
     C_name= models.TextField()
     time = models.TextField()
     loc = models.TextField()
     quantity = models.IntegerField()
     rate = models.IntegerField()
     value = models.IntegerField()
     date = models.DateField()


    
def __str__(self):
        return self.email
    
