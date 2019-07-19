from django import forms
from .models import Post, Comment, CommentReply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['contents']