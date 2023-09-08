from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Category, Comment
from .forms import CommentForm, PostForm


class PostList(ListView):
    """connects Comment to ListView function """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'roadtrips.html'
    paginate_by = 6


class PostDetail(View):
    """connects Post to View function """
    def get(self, request, pk, *args, **kwards):
        # status=1 to get only published posts
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    """Displays the comment section on the PostDetail View Page"""
    def post(self, request, pk, *args, **kwards):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm
            },
        )


def form_valid(self, form):
    """ validates form and connects to user """
    comment_form.instance.created_by = self.request.user
    return super().form_valid(form)


class PostLike(View):
    """connects PostLike to View function """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))


class PostCreate(CreateView):
    """connects Comment to CreateView function """
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your post has been successfully created.')
        return response

class PostUpdate(UpdateView):
    """connects Post to UpdateView function """
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your post has been successfully updated.')
        return response


class PostDelete(DeleteView):
    """connects Post to DeleteView function """
    model = Post
    form_class = PostForm
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Your post has been successfully deleted.')
        return response
