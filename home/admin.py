from django.contrib import admin
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
class ContactView(admin.ModelAdmin):
    list_display = ['Name','cnic','address',
    'organization','contact_number','checkin','checkout',
    'contact_person','purpose','img_location']