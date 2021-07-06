from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=200,default=None)
    password = models.CharField(max_length=200,default=None)
    name = models.CharField(max_length=200,default=None,null=True)
    address = models.CharField(max_length=200,default=None,null=True)
    organization = models.CharField(max_length=200,default=None,null=True)
    contact_number = models.CharField(max_length=200,default=None,null=True)
    checkin = models.CharField(max_length=200,default=None,null=True)
    checkout = models.CharField(max_length=200,default=None,null=True)
    contact_person = models.CharField(max_length=200,default=None,null=True)
    purpose = models.CharField(max_length=200,default=None,null=True)
    img_location = models.CharField(max_length=200,default=None,null=True)
    def __str__(self):
        return self.email