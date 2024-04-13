from django.contrib import admin
from .models import Comment,Reply,Reaction,AnonymousLike

# Register your models here.

admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Reaction)
admin.site.register(AnonymousLike)
# admin.site.register(ReactionType)
