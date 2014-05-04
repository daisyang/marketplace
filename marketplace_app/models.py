from django.db import models
from django.utils import timezone
# Create your models here.

HIGH_SCHOOL = 'HI'
ELEMENTARY_SCHOOL = 'EL'
MIDDLE_SCHOOL = 'MI'
SCHOOL_CHOICES = (
    (HIGH_SCHOOL, 'High school'),
    (ELEMENTARY_SCHOOL,'Elementary school'),
    (MIDDLE_SCHOOL,'Middle school'),
)

class School (models.Model):
    def __unicode__(self):              #  on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField(max_length=200,null=True,blank=True)
    funding_amount = models.FloatField(null=True,blank=True)
    rating = models.IntegerField(default = 0)


class Provider (models.Model):
    def __unicode__(self):              #  on Python 2
        return self.name + str(self.id)

    class Meta:
        ordering = ('name',)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField(max_length=200,null=True,blank=True)
    contract = models.CharField(max_length=50,null=True,blank=True)
    perception = models.CharField(max_length=200,null=True,blank=True)
    target_schools = models.ManyToManyField(School,null=True,blank=True)
    time_start= models.DateTimeField('date start',null=True,blank=True)
    time_end = models.DateTimeField('date end',null=True,blank=True)
    school_level = models.CharField(max_length=2,choices = SCHOOL_CHOICES,default=HIGH_SCHOOL,null=True,blank=True)
    funding_amount = models.FloatField(null=True,blank=True)
    non_profit = models.BooleanField(default=True)
    rating= models.IntegerField(default = 0)



