from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name='profile') #Imports the overrode User from settings, not directly from other app. This way the Entries app is standalone.
    avatar = models.ImageField(upload_to='avatars/', default='defaults/avatar.jpg')
    bio = models.TextField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    joined = models.DateField(auto_now_add=True)

    def __str__(self): #If portrayed in a string, it returns the users username, followed by: 's profile
        return f"{self.user.username}'s profile"

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE, 
                                related_name='entry') #Imports the overrode User from settings, not directly from other app. This way the Entries app is standalone.
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='entries/', default='defaults/entry.jpg')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self): #If portrayed in a string, it returns the entry's title
        return self.title
    
    class Meta:
        ordering = ['-date'] #Orders the dates backwards, so new entries with newer dates are added on top
