from django import forms
from .models import Post,Tag,Categorys
# from django.utils import timezone
# from django.conf import settings
# import os
# from django.forms import ClearableFileInput



# class NewPostForm(forms.ModelForm):
#     files = forms.FileField(required=True)
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'caption'}), required=True)
#     category = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'caption'}), required=True)
#     video_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'caption'}), required=True)
#     content = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'caption'}), required=True)
#     tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Tags - Seperate with comma'}), required=True)
    
#     class Meta:
#         model = Post
#         fields = ['files', 'title', 'tags','category','video_url','content']
# choices = Categorys.objects.all().values_list( 'name','name')  

# choices_list = []      

# for item in choices:
#     choices_list.append(item)


class NewPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Title'}), required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder':'Content'}), required=True)
    # tag_choices = Tag.objects.all().values_list('title', 'title')
    # tags = forms.MultipleChoiceField(choices=tag_choices, widget=forms.SelectMultiple(attrs={'class': 'select', 'placeholder': 'Tag'}), required=False)
    # tags = forms.CharField(widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Tags | Seperate with comma'}), required=True)
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['tags'].widget.choices = self.get_tag_choices()

    # def get_tag_choices(self):
    #     # Fetch tags from the database and return them as choices for the select field
    #     tags = Tag.objects.all().values_list('title', 'title')
    #     return tags
    
    # Retrieve choices dynamically from the database
    categories = Categorys.objects.all().values_list('name', 'name')
    category = forms.ChoiceField(choices=categories, widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Category'}), required=False)
    # picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-upload'}), required=True)  # Add class to ImageField
    
    class Meta:
        model = Post
        fields = [ 'picture','title', 'content', 'tag', 'category']
        
# class EditPostForm(forms.ModelForm):
#     picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image-upload'}), required=True)  # Add class to ImageField
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Title'}), required=True)
#     content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder':'Content'}), required=True)
    
#     tag = forms.CharField(widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Tags | Seperate with comma', 'multiple': 'multiple'}), required=True)
    
#     # Retrieve choices dynamically from the database
#     categories = Category.objects.all().values_list('name', 'name')
#     category = forms.ChoiceField(choices=categories, widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Category'}), required=False)
    
    
#     class Meta:
#         model = Post
#         fields = ['picture','title', 'content', 'tag', 'category', ]
        
    
    

class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Search by title'}),
        label='Search by title',
        required=True,
        max_length=100
    )
        