from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profiles within the app are represented by this model.

    It stores non-auth related information about a user and is auto-created
    when the User model emits a post-save signal.
    """

    avatar = models.ImageField(upload_to='avatars/',
                               default='avatars/default-user.png')
    website = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=160, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    following = models.ManyToManyField('self',
                                       symmetrical=False,
                                       related_name='followers')


class Image(models.Model):
    """User-uploaded images is represented by this model."""

    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField(max_length=280, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Like(models.Model):
    """Likes are tracked by this intermediary model.

    It maintains a relationship with both Image and Profile models.
    """

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comment(models.Model):
    """Comments are represented by this model.

    It maintains a relationship with both Image and Profile models.
    """

    comment = models.CharField(max_length=280)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
