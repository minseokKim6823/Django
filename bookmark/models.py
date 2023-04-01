from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField('url',unique=True)#null=True, blank=True가 아니어서 굵게표시됨
    
    def __str__(self):
        return self.title
