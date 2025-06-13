from django.db import models
# We are going to use Django's built in User Model, so now we need to import it
from django.contrib.auth.models import User
from datetime import datetime


def user_directory_path(instance, filename):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    extension = filename.split('.')[-1]
    return f"profile_pics/user_{instance.user.id}_{timestamp}.{extension}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to=user_directory_path)
    total_weight_lifted = models.PositiveIntegerField(default=0)
    workouts_tracked = models.PositiveIntegerField(default=0)
    personal_tagline = models.TextField(max_length=160, help_text="Type your personal quote / favorite life quote")

    def __str__(self):
        return f"{self.user.username}'s profile"
