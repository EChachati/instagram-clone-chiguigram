from django.contrib.auth.models import User
from django.db import models as m


# Create your models here.
class Profile(m.Model):
    """Proxy model uses Abstract class User and added needed info"""

    user = m.OneToOneField(User, on_delete=m.CASCADE)  # Check Documentation

    # new fields
    website = m.URLField(max_length=250, blank=True)
    biography = m.TextField(blank=True)
    phone_number = m.CharField(max_length=20, blank=True)
    profile_picture = m.ImageField(
        upload_to="users/pictures",
        blank=True,
        null=True
    )
    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
