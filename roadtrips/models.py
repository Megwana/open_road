from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default=True, null=False)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

# class Comment(models.Model):
#     """ Handles comments model """

#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         related_name='comments'
#         )
#     name = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         max_length=30,
#         related_name='comment_author'
#         )
#     email = models.EmailField()
#     body = models.TextField(max_length=400)
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         """
#         Order of comments, oldest first,
#         and return comment
#         """
#         ordering = ['created_on']

#     def __str__(self):
#         """ Returns comment with name and comment body"""
#         return f"Comment {self.body} by {self.name}"

#     def get_absolute_url(self):
#         """ Returns comment with primary key"""
#         return reverse('post_detail', kwargs={'pk': self.pk})
