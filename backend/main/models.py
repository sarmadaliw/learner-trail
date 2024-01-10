from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    """A subject the user is learning about."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of subject."""
        return self.text[:50]
    
class Topic(models.Model):
    """A specific topic about the subject user is learning about."""
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return a string representation of Topic."""
        return self.text[:80]

class Entry(models.Model):
    """Entries specific to the topic user is learning about."""
    subject = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
	    verbose_name_plural = "entries"

