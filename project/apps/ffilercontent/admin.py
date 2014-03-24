from django.contrib import admin
from .models import Content,Image
from apps.django_ffiler.admin import ImageInlineAdmin


class ContentImages(ImageInlineAdmin):
    model = Image


class ContentAdmin(admin.ModelAdmin):
    inlines = [ContentImages]


admin.site.register(Content, ContentAdmin)