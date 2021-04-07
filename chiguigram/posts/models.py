"""[Post models Django]"""

from django.db import models as m
from django.contrib.auth.models import User

from users.models import Profile


class Post(m.Model):
    """ Posts Models
    Must be enlaced with Users
    """
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    profile = m.ForeignKey(Profile, on_delete=m.CASCADE)

    title = m.CharField(max_length=255)
    photo = m.ImageField(upload_to='posts/photos')

    created = m.DateTimeField(auto_now_add=True)
    modified = m.DateTimeField(auto_now=True)

    def __str__(self):
        return f' {self.title} by @{self.user.username}'
