from django.db import models
from django.utils import timezone
# Create your models here.

class Provider (models.Model):
    HIGH_SCHOOL = 'HI'
    ELEMENTARY_SCHOOL = 'EL'
    MIDDLE_SCHOOL = 'MI'
    SCHOOL_CHOICES = (
            (HIGH_SCHOOL, 'High shool').
            (ELEMENTARY_SCHOOL,'Elementary school'),
            (MIDDLE_SCHOOL,'Middle school'),

            )

	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
        website = models.URLField(max_length=200)
        contract = models.CharField(max_length=50)
        perception = models.CharField(max_length=200)
        target_schools = 
        time_start= models.DateTimeField('date start')
        time_end = models.DateTimeField('date end')
        school_level = models.CharField(max_length=2,choices = SCHOOL_CHOICES,default=HIGH_SCHOOL)
        funding_amount = models.FloatField()
        non_profit = models.BooleanField()



