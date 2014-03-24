from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)


class Image(models.Model):
    content = models.ForeignKey(Content)
    image = models.ImageField(upload_to='ffiler_files/')