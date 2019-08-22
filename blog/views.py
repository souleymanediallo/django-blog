from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def home(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")


def post_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)
    context = {'posts': posts, 'categories': categories, 'category': category}
    return render(request, "blog/post_list.html", context)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {'post': post}
    return render(request, "blog/post_detail.html", context)