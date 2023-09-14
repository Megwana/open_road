"""
This module provides forms for handling Post and Comment objects.
It retrieves category names from the Category model to be used as
choices in the PostForm.
"""

from .models import Comment, Post, Category
from django import forms


class PostForm(forms.ModelForm):
    """
    A form for creating or updating a Post.
    The form is designed with specific widgets and attributes to enhance
    user experience and collect the required information for the Post model.
    """
    class PostForm(forms.ModelForm):
        category = forms.ChoiceField(
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = (
            # Fetch ID, Name pairs
            [(cat.id, cat.name) for cat in Category.objects.all()]
        )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and (
            title.isnumeric() or not any(c.isalpha() for c in title)
        ):
            raise forms.ValidationError(
                "Title cannot be exclusively numbers or "
                "non-alphanumeric characters."
                )
        return title

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
            # # Dropdown selection for post category.
            # 'category': forms.Select(
            #     choices=choices,
            #     attrs={'class': 'form-control'}
            # ),
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
