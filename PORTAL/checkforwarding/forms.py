from django import forms
from .models import Post

class ContentsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
