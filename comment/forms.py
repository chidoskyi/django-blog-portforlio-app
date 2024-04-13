from django import forms
from django.core.exceptions import ValidationError
from comment.models import Comment,Reply

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Retrieve user object from kwargs
        super().__init__(*args, **kwargs)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not self.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data
    
    class Meta:
        model = Comment
        fields = ['body','email','name']
        
    
    
class ReplyForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'comment'}), required=True)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Retrieve user object from kwargs
        super().__init__(*args, **kwargs)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not self.user.is_authenticated and data.lower().strip() == 'samuel':
            raise ValidationError("Sorry, you cannot use this name.")
        return data
    
    class Meta:
        model = Reply
        fields = ['body','email','name']