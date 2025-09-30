from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
from .forms import PostForm


# Create your views here.
def posts(request):
    r = requests.get("http://127.0.0.1:8000/posts")
    return render(request, template_name="posts.html", context={"posts": r.json()})

def post(request, post_id):
    r = requests.get(f"http://127.0.0.1:8000/posts/{post_id}")
    return render(request, template_name="post.html", context={"post": r.json()})


@login_required
def post_new(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        payload = {
            "title": form.cleaned_data['title'],
            "body": form.cleaned_data['body'],
        }
        headers = {"Authorization": f'Token {request.user.api_token}'}

        requests.post("http://127.0.0.1:8000/posts/", data=payload, headers=headers)
        return redirect('posts')
    return render(request, template_name="post_form.html", context={"form": form})