"""
This module provides forms for handling Post and Comment objects.
It retrieves category names from the Category model to be used as
choices in the PostForm.
"""

from .models import Comment, Post, Category
from django import forms

choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    """
    A form for creating or updating a Post.
    The form is designed with specific widgets and attributes to enhance
    user experience and collect the required information for the Post model.
    """
    class Meta:
        model = Post
        fields = [
            'title', 'author', 'excerpt', 'category',
            'featured_image', 'content'
        ]
        # Define widgets to control how each form field is displayed.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # The author field is hidden as it's typically
            # populated programmatically.
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'hide-author',
                'type': 'hidden'
            }),
            # Dropdown selection for post category.
            'category': forms.Select(
                choices=choices,
                attrs={'class': 'form-control'}
            ),
            # File input for uploading an image.
            'featured_image': forms.FileInput(
                attrs={'class': 'form-control-file'}
            ),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    A form for users to add comments to a post.
    Users can add a body of text as their comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)
