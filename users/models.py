from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
            return f'{self.user.username} Profile'
        
    #The following is for heroku deployment. For Linux deployment,
    #Do not comment these out
    
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #     if img.width>300 or img.height>300:
    #         output = (300,300)
    #         img.thumbnail(output)
    #         img.save(self.image.path)
        
        
        