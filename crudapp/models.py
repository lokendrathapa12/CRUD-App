from django.db import models

# Create your models here.
class userModel(models.Model):
    Full_Name = models.CharField(max_length=70)
    Email = models.EmailField(max_length=70)
    Address = models.CharField(max_length=70)
    Phone_Number = models.BigIntegerField()
    Birth_Date = models.DateField()
    
    def __str__(self):
        return self.Full_Name