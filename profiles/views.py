from django.views.generic import DetailView
from .models import Profile
# from django.urls import reverse

# Create your views here.

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    context_object_name = "profile"
    queryset = Profile.objects.all()
    #pk_url_kwarg = 'pk'