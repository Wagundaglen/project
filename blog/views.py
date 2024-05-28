# blog/views.py

from django.shortcuts import render, redirect
from .forms import SubscriberForm
from .models import Post

def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SubscriberForm()

    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'form': form, 'posts': posts})
