from django.db import models
from django.utils.encoding import smart_unicode
from time import time
from django.core.validators import MaxValueValidator
# Create your models here.

TYPE_CHOICES = (
    ('Rent', 'Rent'),
    ('Sell', 'Sell'),
    ('Rent Freebies', 'Rent Freebies'),
    ('Sell Freebies', 'Sell Freebies'),
)

CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Sports', 'Sports'),
    ('Books', 'Books'),
    ('Accessories', 'Accessories'),
    ('Bikes', 'Bikes'),
    ('Furniture', 'Furniture'),
    ('Gaming', 'Gaming'),
    ('Apparels', 'Apparels'),
    ('Footwear', 'Footwear'),
    ('Musical Instruments', 'Musical Instruments'),
    ('Bikes/Vehicles', 'Bikes/Vehicles'),
    ('Miscellaneous', 'Miscellaneous'),
)

def get_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)


class PostTable(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    User_ID = models.CharField(max_length=30)
    Email_ID = models.EmailField(max_length=30)
    WhichType = models.CharField(max_length=20, choices=TYPE_CHOICES)
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    Title = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=12, decimal_places=2)
    Description = models.TextField(max_length=256, null=True)
    Location = models.CharField(max_length=20)
    Post_Date = models.DateField(auto_now_add=True)
    Sell_Date = models.DateField(null=True, blank=True)
    Start_Date = models.DateField(null=True, blank=True)
    End_Date = models.DateField(null=True, blank=True)
    Edit_Date = models.DateField(auto_now_add=True)
    Contact_Number = models.CharField(max_length=10, null=True, blank=True)
    Photo_1 = models.FileField(upload_to=get_file_name, null=True, blank=True)
    Photo_2 = models.FileField(upload_to=get_file_name, null=True, blank=True)
    Photo_3 = models.FileField(upload_to=get_file_name, null=True, blank=True)
    Photo_4 = models.FileField(upload_to=get_file_name, null=True, blank=True)
    Photo_5 = models.FileField(upload_to=get_file_name, null=True, blank=True)
        
    def __unicode__(self):
        return smart_unicode(self.Title)