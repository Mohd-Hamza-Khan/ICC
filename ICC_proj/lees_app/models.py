from django.db import models
# import datetime

# Create your models here.
    
    
class Student(models.Model):
    enrollment_no = models.IntegerField(default=0)
    dept = models.CharField(max_length=30, null=True,blank=True)
    year = models.IntegerField(default=0)
    purpose = models.CharField(max_length=100)
    entry = models.TimeField(auto_now=True)
    # exit = datetime(auto_now=True)
    
    
    def __str__(self):
        return "%d %d %s" %(self.enrollment_no, self.year, self.dept)
    