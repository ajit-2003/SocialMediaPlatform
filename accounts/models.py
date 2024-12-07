from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    # Use 'db_table' option to specify the actual table name in the database
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'accounts_profile'  # Specify the actual table name

    def __str__(self):
        return self.user.username
