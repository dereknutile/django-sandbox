from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = FilerImageField(null=True, blank=True, related_name="company_logo")
    disclaimer = FilerFileField(null=True, blank=True)