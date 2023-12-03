from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Define a Post model, which represents a blog post in the database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

     # The string representation of a post will be its title
    def __str__(self):
        return self.title
    # A method to return the absolute URL for a post instance
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
