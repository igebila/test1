from django.db import models
from django.utils import timezone

##################################################  Class For Functionalities ##################################################
# Book Class
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
   
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

# Video Class
class Video(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    vid = models.FileField(upload_to='video/vid/')
    cover = models.ImageField(upload_to='video/cover/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)

    def __str__(self):
        return self.title

# News Class    
class News(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    detail = models.TextField()
    cover = models.ImageField(upload_to='video/cover/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.title

##################################################  PAGES-MODELS ##################################################

# Home Model
class Home(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)

# About Model
class About(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)

# Contactus Model
class Contactus(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,null=True)