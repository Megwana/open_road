from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import CommentForm, PostForm


class PostList(ListView):
    """
    Displays a list of posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'roadtrips.html'
    paginate_by = 6


class PostDetail(View):
    """
    Displays the details of a post including comments and provides
    functionality to add a new comment.
    """

    def get(self, request, pk, *args, **kwargs):
        """Renders the post detail page."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = post.likes.filter(id=request.user.id).exists()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, pk, *args, **kwargs):
        """Handles the creation of a new comment for the post."""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = post.likes.filter(id=request.user.id).exists()
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(
                request,
                'Comment added successfully and waiting for admin approval!'
                )
        else:
            messages.error(
                request,
                'Failed to add comment. Please enter valid input.'
            )

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class PostLike(View):
    """
    Handles the logic for users to like or unlike a post.
    """

    def post(self, request, slug):
        """Toggles the 'like' status for a post."""
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'Like successfully removed!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'Like successfully added!')
        return HttpResponseRedirect(
            reverse_lazy('post_detail', args=[post.pk])
        )


class PostCreate(CreateView):
    """
    Displays a form for creating a new post and saves it upon submission.
    """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        """Overrides form_valid to add a success message."""
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Post created successfully!')
            return response
        except Exception as e:
            messages.error(self.request, f"Failed to create post. Error: {e}")


class PostUpdate(UpdateView):
    """
    Displays a form for updating an existing post and updates it upon
    submission.
    """
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'

    def form_valid(self, form):
        """Overrides form_valid to add a success message."""
        try:
            response = super().form_valid(form)
            messages.success(self.request, 'Post updated successfully!')
            return response
        except Exception as e:
            messages.error(self.request, f"Failed to update post. Error: {e}")


class PostDelete(DeleteView):
    """
    Displays a confirmation prompt before deleting a post and deletes it upon
    confirmation.
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        """Overrides delete to add a success message."""
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(self.request, 'Post deleted successfully!')
            return response
        except Exception as e:
            messages.error(self.request, f"Failed to delete post. Error: {e}")
            return HttpResponseRedirect(
                self.success_url
            )  # redirect back to the same page
