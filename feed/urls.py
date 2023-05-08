from django.urls import path
from .views import HomePage, PostDetailView, NewPost

app_name = "feed"

urlpatterns = [
    path("", HomePage.as_view(), name = "index"),
    path("<int:pk>/", PostDetailView.as_view(), name = "detail"),
    path("newpost/", NewPost.as_view(), name = "post")
    
]
