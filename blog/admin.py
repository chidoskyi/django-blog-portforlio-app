from django.contrib import admin
from .models import Tag, Post,Like,Visit,Categorys
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Categorys)
admin.site.register(Like)
admin.site.register(Visit)
# admin.site.register(PostFileContent)
