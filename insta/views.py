from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'instablog/home.html',context=context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','image']
    template_name = 'instablog/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content','image']
    template_name = 'instablog/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostListView(LoginRequiredMixin,ListView):
    login_url = '/logout/'
    redirect_field_name = '/'
    model = Post
    template_name = 'instablog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class UserList(LoginRequiredMixin,ListView):
    login_url = '/logout/'
    redirect_field_name = '/'
    model = Post
    template_name = 'instablog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'instablog/post_detail.html'

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'instablog/post_delete.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



def about(request):
    return render(request,'instablog/about.html',{'title':'About Page'})
