from django.views.generic import DetailView
from .models import Profile
from feed.models import Post


# Create your views here.

class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = "profile_detail.html"
    model = Profile
    context_object_name = "profile"
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        posts = Post.objects.filter(author=profile.user)
        context['posts'] = posts
        return context
   
    