from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import PostForm

# Create your views here.


def loginView(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR Password is not correct!')

    context = {'page': page}
    context = {}

    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('index')


def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index', )  # Change 'post_detail' to your actual detail view name
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def blog(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog.html', context)

