from django.db import models
from apps.thumbz.thumbs import ImageWithThumbsField

class Person(models.Model):
    name = models.CharField(max_length=255)
    someimage = ImageWithThumbsField(upload_to='images', sizes=((150,150),(300,200)))
    somefile = models.FileField(upload_to='files')