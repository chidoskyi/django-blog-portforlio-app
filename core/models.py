from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# from blog.models import Post
from PIL import Image
from django.db.models.signals import post_save


# Create your models here.

# uploading users file to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=user_directory_path, null=True, verbose_name='Picture', blank=True,
                              default="default.jpg")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - Profile'

        # def save(self, *args, **kwargs):
        #     super().save(*args, **kwargs)
        #     SIZE = 300, 300

        if self.image:
            # image = Image.open(self. image.path)
            # image.thumbnail(SIZE, Image.LANCZOS)
            # image.save(self.image.path)

            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)  # Add a name field
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Home(models.Model):
    greetings = models.CharField( max_length=50)
    description = models.CharField( max_length=10000)
    home_img = models.ImageField(upload_to='picture_home/')
    time_added = models.DateTimeField(auto_now=True)
    
class About(models.Model):
    name = models.CharField( max_length=50)
    title = models.CharField( max_length=50)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True )
    
    def __str__(self) -> str:
         return self.name + ' - ' + str(self.updated)

class ProfileInfo(models.Model): 
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name = 'profileinfo') 
    birthday = models.DateField()
    website = models.CharField(max_length=100)
    degree = models.CharField( max_length=500)
    city = models.CharField( max_length=500)
    country = models.CharField( max_length=500)
    email = models.CharField( max_length=500)
    phone = models.CharField( max_length=500)
    freelance = models.CharField( max_length=500)
    # updated = models.DateTimeField(auto_now=True )
    
    @property
    def age(self):
        today = datetime.now().date()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age
    
class ProgressModel(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name = 'progressbar')
    title = models.CharField( max_length=100)
    count = models.PositiveSmallIntegerField(default=0)
    # updated = models.DateTimeField(auto_now=True)
    
    
class Education(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name = 'education')
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    course = models.CharField( max_length=150)
    description = models.TextField()
    
class Experience(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name = 'experience')
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    course = models.CharField( max_length=150)
    description = models.TextField()
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    details_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Portfolio {self.id}"
    
class ContactInfo(models.Model):
    phone = models.CharField( max_length=500)
    email_info = models.CharField( max_length=500)
    office = models.CharField( max_length=500)
    website = models.CharField( max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'ContactInfo {self.id}'
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    

    def __str__(self):
        return self.name