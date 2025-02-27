from django.shortcuts import render
from .models import Post


def chat(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'chat.html', {'posts': posts})


from django.shortcuts import render

# Create your views here.
