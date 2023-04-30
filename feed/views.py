from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomePage(ListView):
    http_method_names = ['get']
    template_name = "homepage.html"
    model = Post
    queryset = Post.objects.all().order_by("-id")
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    http_method_names = ['get']
    template_name = "detail.html"
    model = Post
    context_object_name = "post"
    