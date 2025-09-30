from django.shortcuts import render
import requests


# Create your views here.
def posts(request):
    r = requests.get("http://127.0.0.1:8000/posts")
    return render(request, template_name="posts.html", context={"posts": r.json()})

def post(request, post_id):
    r = requests.get(f"http://127.0.0.1:8000/posts/{post_id}")
    return render(request, template_name="post.html", context={"post": r.json()})
