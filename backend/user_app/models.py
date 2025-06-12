from django.db import models
# We are going to use Django's built in User Model, so now we need to import it
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    total_weight_lifted = models.IntegerField()
    personal_tagline = models.TextField(max_length=400)