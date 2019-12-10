from django.db import models

# Create your models here.
class emp (models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=30)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=10)
    
    class Meta:
        db_table="emp"