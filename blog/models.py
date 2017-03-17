from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class Custom_User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M', null=False)
    email_id = models.EmailField(primary_key = True)
    phone_nnumber = models.IntegerField()
    spouse_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.email_id
