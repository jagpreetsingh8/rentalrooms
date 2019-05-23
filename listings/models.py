from django.db import models
from datetime import datetime
from owner.models import Owner
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

DEFAULT_EXAM_ID = 1
class Listing(models.Model):
    owner = models.ForeignKey(Owner,default =DEFAULT_EXAM_ID, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    parking = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    security_fee = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.photo_main = self.compressImage(self.photo_main)
    #     super(Listing, self).save(*args, **kwargs)
    
    # def compressImage(self,photo_main):
    #     imageTemproary = Image.open(photo_main)
    #     outputIoStream = BytesIO()
    #     imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
    #     imageTemproary.save(outputIoStream , format='JPEG', quality=60)
    #     outputIoStream.seek(0)
    #     photo_main = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % photo_main.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    #     return photo_main
    
    def save(self):
        if not self.photo_main:
            return            

        super(Listing, self).save()
        photo_main = Image.open(self.photo_main)
        (width, height) = photo_main.size     
        size = ( 1920, 1258)
        photo_main = photo_main.resize(size, Image.ANTIALIAS)
        photo_main.save(self.photo_main.path)