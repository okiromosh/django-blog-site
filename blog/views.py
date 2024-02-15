from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('index', )  # Change 'post_detail' to your actual detail view name
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)
