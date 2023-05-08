from django.urls import path
from .views import ProfileDetailView

app_name = "profiles"

urlpatterns = [
    path("<int:pk>/", ProfileDetailView.as_view(), name = "detail")
]
