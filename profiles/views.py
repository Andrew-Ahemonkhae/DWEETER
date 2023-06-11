from django.views.generic import DetailView
from .models import Profile
from followers.models import Follower
from feed.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = "profile_detail.html"
    model = Profile
    context_object_name = "profile"
    
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        posts = Post.objects.filter(author=profile.user).count()
        context['posts'] = posts
        if self.request.user.is_authenticated:
            is_following = self.is_following(self.request.user, profile.user)
            context['you_follow'] = is_following
            
        return context
    
    def is_following(self, user, profile_user):
        try:
            following = Follower.objects.get(following=profile_user, followed_by=user)
            return True
        except Follower.DoesNotExist:
            return False
   
    