from django import forms

from .models import Post, Comment, Review

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('author', 'text',)
