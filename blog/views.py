from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, year, month, day, slug):
    post = Post.objects.filter(
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug
    ).first()
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )