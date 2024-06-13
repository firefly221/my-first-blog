from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(req):
    posts= Post.objects.all()
    return render(req,'blog/post_list.html',{'posts' : posts})


