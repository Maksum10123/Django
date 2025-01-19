from django.shortcuts import render
from .models import Post, Author

# Create your views here.
def main(request):
    posts = Post.objects.filter(published=True)
    return render(request, "main_page", {"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail_view")