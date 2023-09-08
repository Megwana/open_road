from .models import Comment, Post, Category
from django import forms

choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = fields = ['title', 'author', 'excerpt', 'category',
                           'featured_image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'hide-author',
                'type': 'hidden'
            }),
            'category': forms.Select(
                choices=choices,
                attrs={'class': 'form-control'}
            ),
            'featured_image': forms.FileInput(
                attrs={'class': 'form-control-file'}
            ),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
