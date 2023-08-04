from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/images',null=True)
    video = models.FileField(upload_to='media/videos/',null=True, blank=True)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()  # Add this field
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        
        return self.name