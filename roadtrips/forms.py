"""
This module provides forms for handling Post and Comment objects.
"""

from .models import Comment, Post, Category
from django import forms


class PostForm(forms.ModelForm):
    """
    A form for creating or updating a Post.
    """
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Directly fetch ID and Name pairs from Category
        self.fields['category'].choices = Category.objects.values_list(
            'id',
            'name'
            )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and (
            title.isnumeric() or not any(c.isalpha() for c in title)
        ):
            raise forms.ValidationError(
                "Title cannot be exclusively numbers"
                "or non-alphanumeric characters."
            )
        return title

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'excerpt',
            'category',
            'featured_image',
            'content'
            ]
        #  Define widgets to control how each form field is displayed.
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
            'featured_image': forms.FileInput(
                attrs={'class': 'form-control-file'}
                ),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    A form for users to add comments to a post.
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
