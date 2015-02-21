from django.db import models

# Create your models here.

class employment(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=9, decimal_places=6,default=0)


