from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# from notification.models import Notification

# Create your models here.


# class Comment(models.Model):
#      post = models.ForeignKey(Post, related_name = 'comments', on_delete=models.CASCADE)
#      user = models.ForeignKey(User, on_delete=models.CASCADE)
#      name = models.CharField(max_length=100)
#      email = models.EmailField()
#      body = models.TextField()
#      likes = models.PositiveIntegerField(default=0)
#      date = models.DateTimeField(auto_now_add=True)
     
     
     
#      def user_comment_post(sender, instance, *args, **kwargs):
#         comment = instance
#         post = comment.post
#         text_preview = comment.body[:90]
#         sender = comment.user
#         # notify = Notification(post=post, sender=sender, user=post.user, text_preview=text_preview, notification_types=2)
#         # notify.save()

#      def user_del_comment_post(sender, instance, *args, **kwargs):
#         comment = instance
#         post = comment.post
#         sender = comment.user
#         # notify = Notification.objects.filter(post=post, sender=sender, user=post.user, notification_types=2)
#         # notify.delete()

# class Reply(models.Model):
#     comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     date = models.DateTimeField(auto_now_add=True)
#     likes = models.PositiveIntegerField(default=0)
    
#     def __str__(self):
#         return f'Reply by {self.user.username} on {self.date}'

# post_save.connect(Comment.user_comment_post, sender=Comment)
# post_delete.connect(Comment.user_del_comment_post, sender=Comment)

class Reaction(models.Model):
    LIKE = '👍'
    UNLIKE = '👎'
    LOVE = '❤️'
    WOW = '😲'
    SAD = '😢'
    HAPPY = '🤣'
    ANGRY = '😡'
    SUPPORT = '❤️‍🩹'
    CARE = '🤗'

    REACTION_CHOICES = [
        (LIKE, '👍'),  # Like
        (UNLIKE, '👎'),  # Unlike
        (LOVE, '❤️'),  # Love
        (WOW, '😲'),   # Wow
        (SAD, '😢'),   # Sad
        (HAPPY, '🤣'),  # Happy
        (ANGRY, '😡'),  # Angry
        (SUPPORT, '❤️‍🩹'),  # Support
        (CARE, '🤗'),  # Care
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comment_reactions', null=True, blank=True)
    reply = models.ForeignKey('Reply', on_delete=models.CASCADE, related_name='reply_reactions', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_reactions', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.reaction_type
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, verbose_name='comment_likes', related_name='comment_likes')
    
    
    
    class Meta:
        ordering = ['-date'] 
    
    def totals_likes(self):
        return self.likes.count()
    
    def get_reaction_choices(self):
        reaction_choices = []
        for reaction_type_display, reaction_type_value in Reaction.REACTION_CHOICES:
            reaction_count = self.comment_reactions.filter(reaction_type=reaction_type_value).count()
            reaction_choices.append((reaction_type_display, reaction_count))
        return reaction_choices
    
    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return self.name if self.name else "Anonymous"
    
    def clean(self):
        if self.user and self.name:
            raise ValidationError("Either provide a user or a name, not both.")
        
        email = self.email
        if not email:
            raise ValidationError("Email field cannot be empty.")
        
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, verbose_name='reply_likes', related_name='reply_likes')
    
    class Meta:
        ordering = ['-date']  # Orders by the 'created_at' field in descending order
        
    def total_reply_likes(self):
        return self.likes.count()
    
    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return self.name if self.name else "Anonymous"
    
    def clean(self):
        if self.user and self.name:
            raise ValidationError("Either provide a user or a name, not both.")
        
        email = self.email
        if not email:
            raise ValidationError("Email field cannot be empty.")
        
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")

class AnonymousLike(models.Model):
    reply = models.ForeignKey('Reply', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    # Add any additional fields as needed
    
    @staticmethod
    def total_anonymous_likes(reply):
        return AnonymousLike.objects.filter(reply=reply).count()
    
    



        


