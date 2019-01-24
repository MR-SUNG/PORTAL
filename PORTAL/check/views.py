from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from .models import Post, Comment
from .forms import ContentsForm, CommentForm

# Create your views here.

@login_required
def index(request):
    post_list = Post.objects.all()
    comment_list = Comment.objects.all()

    if request.method == "POST":
        form = ContentsForm(request.POST)
        form2 = CommentForm(request.POST)
        if form.is_valid():
            content = form.save(commit = False)
            content.author = request.user
            content.save()
            return redirect('check:index')
        elif form2.is_valid():
            comment = form2.save(commit = False)
            comment.author = request.user
            comment.save()
            return redirect('check:index') 
    else:
        form = ContentsForm()
        form2 = CommentForm()

    return render(request, 'check/check_list.html', {
            'post_list': post_list, 'comment_list': comment_list, 'form':form, 'form2':form2 })