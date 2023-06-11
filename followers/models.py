from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()

# Create your models here.
class Follower(models.Model):
    followed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followed_by"
    )
    
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "following"
    )
    
    def clean(self):
        if self.following == self.followed_by:
            raise ValidationError("A user cannot follow him or herself!")
        
    def __str__(self):
        return f"{self.following} is being followed by {self.followed_by}"
    
class Meta:
    constraints = [
        models.UniqueConstraint(fields=['followed_by', 'following'], name = 'unique_following')
    ]
    