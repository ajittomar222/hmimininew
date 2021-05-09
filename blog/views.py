from django.shortcuts import render,get_object_or_404 #if user doesn't exists gives 404 error 
from .models import Path
from django.views.generic import (ListView, 
DetailView, 
CreateView,
UpdateView,
DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.http import HttpResponse
# Create your views here.
posts=[
    {
        'Author':'Adwait Patil',
        'Book':'Data Science',
        'date_posted':'1 jan 2019',
        'title':'Post1'
    },
    {
        'Author':'Sameer Mahajan',
        'Book':'Girl Science',
        'date_posted':'24 oct 2019',
        'title':'Post2'
    },
    {
        'Author':'Bharti Jivanani',
        'Book':'EDC',
        'date_posted':'29 feb 2020',
        'title':'Post3'
    }
]

def home(request):
    context={
        'posts': Path.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Path
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #for looping throug all the posts
    ordering = ['date_posted']    # attribute on which ordering is decided
    paginate_by = 3

class UserPostListView(ListView):
    model = Path
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  #for looping throug all the posts
    ordering = ['-date_posted']    # attribute on which ordering is decided
    paginate_by = 3
    def get_queryset(self):
        user = get_object_or_404(User ,username=self.kwargs.get('username'))
        return Path.objects.filter(Author=user).order_by('date_posted')



class PostDetailView(DetailView):
    model = Path
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Path
    fields = ['title','Book','link']
# for removing integrity error
    def form_valid(self,form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = Path
     fields = ['title','Book','link']

     def form_valid(self,form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

     def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Path
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
