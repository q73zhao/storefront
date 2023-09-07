from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):

    label = models.CharField(max_length=255)


class TagItem(models.Model):

    #what tag appleid to what tag

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


    #Generic way of deifining object
    # Type (product, video, article)
    # ID

    content_type  = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() #limitation can only use id as primary key
    content_object = GenericForeignKey()


