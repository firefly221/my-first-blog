from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(req):
    posts= Post.objects.all()
    return render(req,'blog/post_list.html',{'posts' : posts})


def post_detail(req,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(req,'blog/post_detail.html',{'post':post})



