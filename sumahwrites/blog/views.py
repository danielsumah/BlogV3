from django.shortcuts import render, redirect
from .forms import NewUserForm, AddCommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Post, Comment


# Create your views here.

class BlogCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name ='blog_post_comment.html' 
    success_url = '/' 

    def form_valid(self, form):
        form.instance.post__slug = self.kwargs['slug']
        return super().form_valid(form)

    # def form_valid(self, form):
    #     return super(BlogCommentView, self).form_valid(form)

    # def form_invalid(self, form):
    #     post = Post.objects.get(slug=current_slug)
    #     form.instance.post_id = post   
    #     return super().form_invalid(form)

    # def get_initial(self, *args, **kwargs):
    #     initial = super().get_initial(**kwargs)
    #     initial['body'] = 'Enter your comment here'
    #     return initial


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_post_detail.html"
    context_object_name = 'post'

class BlogHomeView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'


def blog_register_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('blog:blog_login_url')
        else:
            messages.info(
                request, 
                "Something is Wrong: \n\n email must be in this format 'xyz@email.com' \n password- 8 digits, Contain Cap Letter and a Number"
                )
        

    context = {'form': form}
    return render(request, 'blog_register.html', context)


def blog_login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:blog_home_url')
        else:
            messages.info(request, 'Username or Password is incorrect ')

    context = {}
    return render(request, 'blog_login.html', context)