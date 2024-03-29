from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, CommentReply
from .forms import PostForm, CommentForm, ReplyForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post' : post})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'new.html', {'form' : form})

def edit(request, post_id):
    post = Post.objects.get(pk = post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'post' : post, 'form' : form})

def delete(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return redirect('/')

def comment_create(request, post_id):
        if request.method == 'POST':
                post = get_object_or_404(Post, pk=post_id)
                form = CommentForm(request.POST)

                if form.is_valid():
                        comment = form.save(commit = False)
                        comment.post = post 
                        comment.save()
                return redirect('/' + str(post.id))
        else:
                form = CommentForm()
                return render(request, 'detail.html', {'form' : form})

def comment_reply(request, post_id, comment_id):
        if request.method == 'POST':
                comment = get_object_or_404(Comment, pk=comment_id)
                form = ReplyForm(request.POST)

                if form.is_valid():
                        reply = form.save(commit = False)
                        reply.comment = comment
                        reply.save()
                return redirect('/' + str(post_id))
        else:
                form = ReplyForm()
                return render(request, 'detail.html', {'form' : form})

def comment_delete(request, post_id, comment_id):
        post = get_object_or_404(Post, pk=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        
        return redirect('/' + str(post.id))

def comment_reply_delete(request, post_id, comment_id, commentReply_id):
        post = get_object_or_404(Post, pk=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        commentReply = get_object_or_404(CommentReply, pk=commentReply_id)
        commentReply.delete()
        
        return redirect('/' + str(post.id))