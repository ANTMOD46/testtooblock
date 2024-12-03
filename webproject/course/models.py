from django.db import models

# Create your models here.
class Course (models.Model):
    Course_id = models.CharField(max_length=128 , primary_key = True)
    Course_name = models.CharField(max_length = 128)
    Teacher_name = models.CharField(max_length = 128)
    



    
