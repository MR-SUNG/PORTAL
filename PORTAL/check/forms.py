from django import forms
from .models import Post, Comment

class ContentsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('kind', 'content',)
        widgets = {
            'content': forms.Textarea(attrs={'cols': 75, 'rows': 6, 'placeholder':"여기에 내용을 입력하세요!",}),       
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message','auto_increment_id')
        widgets = {
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 1, 'placeholder':"댓글쓰기",}),
        }