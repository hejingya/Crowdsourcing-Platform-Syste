from django.db import models

# Create your models here.
class Sponsor(models.Model):
    id = models.AutoField();　
    name = models.CharField(max_length=128);
    phoneNum = models.IntegerField;


    def __str__(self):
        return self.name;