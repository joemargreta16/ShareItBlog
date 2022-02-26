from .forms import UpdateProfilePageForm, UpdateUserPageForm, ChangePasswordForm
from .models import Profile
from blog.models import Comment, User
from blog.views import Post, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by( 'hit_count_generic' )[:4]

    popular_posts_head = Post.objects.order_by( 'hit_count_generic' )[:1]

    page = request.GET.get( 'page' )
    paginator = Paginator( posts, 9 )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        posts = paginator.page( 1 )
    except EmptyPage:
        posts = paginator.page( paginator.num_pages )

    context = {
        'posts': posts,
        'categories': categories,
        'popular_posts': popular_posts,
        'popular_posts_head': popular_posts_head,
    }
    return render( request, 'blog/blog.html', context )

@login_required
def author_profiles(request, id):
    author_profile_page = get_object_or_404(Post, pk=id )
    profile = Profile.objects.get( user=id )
    posts = Post.objects.filter( author=id )
    posts_count = Post.objects.filter( author=id ).count()
    comment_count = Comment.objects.filter( user=id ).count()
    
    page = request.GET.get( 'page' )
    paginator = Paginator( posts, 8 )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        posts = paginator.page( 1 )
    except EmptyPage:
        posts = paginator.page( paginator.num_pages )
    
    context = {
        'author_profile_page': author_profile_page,
        'profile': profile,
        'posts': posts,
        'posts_count': posts_count,
        'comment_count': comment_count,
        'page': page,
    }
    
    return render( request, 'pages/author_profile.html', context )

@login_required
def my_profile(request):
    profile = Profile.objects.get( user=request.user )
    posts = Post.objects.filter( author=request.user )
    posts_count = Post.objects.filter( author=request.user ).count()
    comment_count = Comment.objects.filter( user=request.user ).count()

    page = request.GET.get( 'page' )
    paginator = Paginator( posts, 8 )
    try:
        posts = paginator.page( page )
    except PageNotAnInteger:
        posts = paginator.page( 1 )
    except EmptyPage:
        posts = paginator.page( paginator.num_pages )

    context = {
        'profile': profile,
        'posts': posts,
        'posts_count': posts_count,
        'comment_count': comment_count,
        'page': page,
    }
    return render( request, 'pages/my_profile.html', context )

def password_success(request):
    return render( request, 'pages/password_success.html' )

def portfolio(request):
    return render( request, 'pages/portfolio.html' )

@login_required
def update_profile(request):
    profile = Profile.objects.get( user=request.user )
    u_form = UpdateUserPageForm( request.POST or None, instance=request.user )
    p_form = UpdateProfilePageForm( request.POST or None, request.FILES or None, instance=profile )
    
    confirm = False

    if request.method == 'POST':
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            confirm = True

    context = {
        'profile': profile,
        'u_form': u_form,
        'p_form': p_form,
        'confirm': confirm,
    }
    return render( request, 'pages/myprofile_edit_form.html', context )

class ChangePassword( PasswordChangeView ):
    form_class = ChangePasswordForm
    success_url = reverse_lazy( 'pages:password_success' )