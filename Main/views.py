from django.shortcuts import render, redirect

from Main.models import Category, Post, City


def index(request):
    return render(request, 'index.html',
                  {'categories': Category.objects.all(), 'posts': Post.objects.all(), 'cities': City.objects.all()})


def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'ad.html', {'post': post, 'user_is_owner': post.owner.id == request.user.id})


def sign_up(request):
    return render(request, 'sign_up.html')
