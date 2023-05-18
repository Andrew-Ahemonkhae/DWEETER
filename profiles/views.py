from django.views.generic import DetailView
from .models import Profile
# from django.shortcuts import get_object_or_404
# from django.urls import reverse

# Create your views here.

class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = "profile_detail.html"
    model = Profile
    context_object_name = "profile"
   
    # def get_object(self, queryset=None):
    #     profile_id = self.kwargs.get('profile_id')
    #     return get_object_or_404(Profile, id=profile_id)