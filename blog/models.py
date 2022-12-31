from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image #import Image from PIL pillow lib to modify size of pic
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"author:{self.author.username}"
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='profile_pics')
    def __str__(self):
        return f"username:{self.user.username}"
    # override save method to reduce pixels of larger pics which is unnecessary to avoid overhead
    def save(self,*args, **kwargs):
        super(Profile,self).save(*args, **kwargs) # to avoid force insert
        
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
