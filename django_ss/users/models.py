import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

# Establishes a one-to-one relationship with the User model. 
# If a User is deleted, their corresponding Profile is also deleted.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #check if the image file exists before opening
        if os.path.exists(self.image.path):
            img = Image.open(self.image.path)
            
            # Checks if the image's height or width is greater than 300 pixels.
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)



