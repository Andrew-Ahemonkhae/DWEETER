from django.urls import path
from .views import ProfileDetailView

app_name = "profiles"

urlpatterns = [
   path("user/<int:pk>/", ProfileDetailView.as_view(), name = 'detail'),
]
