from django.shortcuts import render
import requests


# Create your views here.
def posts(request):
    r = requests.get("http://127.0.0.1:8000/posts")
    return render(request, template_name="posts.html", context={"posts": r.json()})
# print(r.json())