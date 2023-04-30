from django.urls import path
from .views import HomePage, PostDetailView

app_name = "feed"

urlpatterns = [
    path("", HomePage.as_view(), name = "index"),
    path("<int:pk>/", PostDetailView.as_view(), name = "detail"),
    
]
