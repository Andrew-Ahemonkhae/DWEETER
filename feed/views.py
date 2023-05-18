from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.urls import reverse_lazy

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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post'] = self.object
    #     return context
    
class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "newpost.html"
    fields = ['text']
    login_url = reverse_lazy('account_login')
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)