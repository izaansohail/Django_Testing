from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=200,default=None)
    password = models.CharField(max_length=200,default=None)
    name = models.CharField(max_length=200,default=None)
    address1 = models.CharField(max_length=200,default=None)
    organization = models.CharField(max_length=200,default=None)
    contact_number = models.CharField(max_length=200,default=None)
    checkin = models.CharField(max_length=200,default=None)
    checkout = models.CharField(max_length=200,default=None)
    contact_person = models.CharField(max_length=200,default=None)
    purpose = models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.email