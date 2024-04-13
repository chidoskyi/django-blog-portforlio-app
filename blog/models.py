from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
import uuid
# from comment.models import GenericRelation,Reaction


# from notification.models import Notification

# Create your models here.

# uploading user files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)




class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tag")
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Tag Images")
    slug = models.SlugField(null=False, unique=True, default=uuid.uuid1) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        # Set the author to the admin user
        admin_user = User.objects.get(username='Netphixs')  # Replace 'admin' with the username of your admin user
        self.author = admin_user
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def get_absolute_url(self):
        return reverse("tags", args=[self.slug])

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Categorys(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category")

    def get_absolute_url(self):
        return reverse("post-list")

    def __str__(self) -> str:
        return self.name

    


# from django.db import models
# from django.contrib.auth.models import User

# class PostFileContent(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
#     file = models.FileField(upload_to=user_directory_path)
    
#     def __str__(self):
#         return self.file.name

#     def save(self, *args, **kwargs):
#         # Extract the request object from kwargs
#         request = kwargs.pop('request', None)
        
#         # If the user is not set and a request object is available, set the user to the current user
#         if not self.user_id and request:
#             self.user = request.user
        
#         super(PostFileContent, self).save(*args, **kwargs)



class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    picture = models.ImageField(upload_to=user_directory_path, verbose_name="Picture")
    tag = models.ManyToManyField(Tag, related_name="posts", verbose_name="Tags")
    category = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, verbose_name='posts_likes', related_name='posts_likes')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])
    
class Visit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title # Customize as per your requirement


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")

    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        # notify = Notification(post=post, sender=sender, user=post.user)
        # notify.save()

    def user_unliked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        # notify = Notification.objects.filter(post=post, sender=sender, notification_types=1)
        # notify.delete()





