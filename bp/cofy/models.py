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

class employment_growth(models.Model):
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

class immigration(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class job_openings(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=9, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class job_seekers(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class occupational_groupings(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    occupational_grouping = models.CharField(max_length=194)
    occupation = models.CharField(max_length=420)

class other_replacement(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class other_seekers(models.Model):
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

class retirements(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class school_leavers(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    y2012 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2013 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2014 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2015 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2016 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2017 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2018 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2019 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2020 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2021 = models.DecimalField(max_digits=8, decimal_places=6,default=0)
    y2022 = models.DecimalField(max_digits=8, decimal_places=6,default=0)

class summary(models.Model):
    noc = models.CharField(max_length=5, primary_key=True)
    employment_in_2012 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    employment_growth_2013_2022 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    retirements_2013_2022 = models.DecimalField(max_digits=4, decimal_places=1,default=0)
    other_replacement_2013_2022 = models.DecimalField(max_digits=4, decimal_places=1,default=0)
    job_openings_2013_2022 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    school_leavers_2013_2022 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    immigrants_2013_2022 = models.DecimalField(max_digits=4, decimal_places=1,default=0)
    job_seekers_other_2013_2022 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    job_seekers_all_2013_2022 = models.DecimalField(max_digits=5, decimal_places=1,default=0)
    labour_market_conditions_2010_2012 = models.CharField(max_length=8)
    projected_labour_market_conditions_2013_2022 = models.CharField(max_length=8)