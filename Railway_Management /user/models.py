from django.db import models
from django.forms.widgets import Widget



class User(models.Model):
    genderTypes = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'None')
    )

    id = models.AutoField(db_column='ID',primary_key=True) 
    name = models.CharField(db_column='Name', max_length=30)  
    email = models.EmailField(db_column='Email', max_length=60)
    contact = models.CharField(db_column='Contact_No', max_length=20)
    gender = models.CharField(choices=genderTypes, max_length=10, default="N")
    usrStatus = models.BooleanField(db_column='Maritial Status')
    age = models.IntegerField(db_column='Age')
    date_of_journey = models.DateField(db_column='Date_Of_Journey') 
    seat = models.FloatField(db_column='Seat')
    coach= models.TextField()
    birthmark = models.TextField(db_column='Birthmark')
    usrImg = models.ImageField(db_column='Usr_Img',upload_to='')

    class Meta:
        db_table = 'user'