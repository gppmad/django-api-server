from django.db import models

# Create your models here.
class Ram(models.Model):
    class Meta:
        db_table = 'app_ram'

    value = models.IntegerField(null=False)
    um = models.CharField(max_length=255,null=False)
    
    def __str__(self):
        return str(str(self.__dict__))