from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from .models import Post
from .forms import ContentsForm

# Create your views here.

@login_required
def index(request):
    post_list = Post.objects.all()
    
    if request.method == "POST":
        form = ContentsForm(request.POST)
        if form.is_valid():
            content = form.save(commit = False)
            content.author = request.user
            content.save()
            return redirect('checkforwarding:index')
    else:
        form = ContentsForm()

    return render(request, 'checkforwarding/index.html', {
            'post_list': post_list, 'form':form
    })
