from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
# Read (List all posts)
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Show latest posts first
    return render(request, 'blogapp/home.html', {'posts': posts})
#Create new post


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        Post.objects.create(user=request.user, title=title, content=content, image=image)  # Assign the user
        return redirect('home')
    return render(request, 'blogapp/create_post.html')


# Update existing post

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)  # Ensure user owns the post
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        if 'image' in request.FILES:  # Allow updating image
            post.image = request.FILES['image']
        post.save()
        return redirect('home')  # Redirect to homepage after updating
    return render(request, 'blogapp/update_post.html', {'post': post})


# Delete post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)  # Ensure user owns the post
    if request.method == 'POST':
        post.delete()
        return redirect('home')  # Redirect to homepage after deleting
    return render(request, 'blogapp/delete_post.html', {'post': post})

