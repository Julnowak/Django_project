from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """ Topic written by user."""
    # Maximum topic text length
    text = models.CharField(max_length=255)

    # Automatically added current date and time to topic
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """ Model representation as string"""
        return self.text
    
class Entry(models.Model):
    """Entries to topics - detailed information"""

    # delete all related
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # No text limits 
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # Nesed class - not to use 'Entrys'
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """ Model representation as string - only first 50 chars"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text