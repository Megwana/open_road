from django.contrib import admin
from .models import Post, Comment, Category
# from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Handle functionalitly of categorys in the admin view """
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Handle functionality of posts in the admin view """
    list_display = ('title', 'slug', 'status', 'created_on', 'content')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    # summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Handle comments by Site_Users """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
