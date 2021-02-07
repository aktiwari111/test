from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post





def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def technicalcourses(request):
    u1 = "https://source.unsplash.com/1600x900/?technology"
    u2 = "https://source.unsplash.com/1600x900/?machine"
    u3 = "https://source.unsplash.com/1600x900/?science"
    u4 = "https://source.unsplash.com/1600x900/?computer"
    u5 = "https://source.unsplash.com/1600x900/?science"
    u6 = "https://source.unsplash.com/1600x900/?coding"
    ls = [u1,u2,u3,u4,u5,u6]
    return render(request, 'blog/technical_courses.html', {'urls': ls})


def front(request):
    u1 = "https://source.unsplash.com/1600x900/?technology"
    u2 = "https://source.unsplash.com/1600x900/?machine,child"
    u3 = "https://source.unsplash.com/1600x900/?school,science"
    ls = [u1, u2, u3]
    
    return render(request, 'blog/front.html', {'urls': ls})
