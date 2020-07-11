from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profiles within the app are represented by this model.

    It stores non-auth related information about a user and is auto-created
    when the User model emits a post-save signal.
    """

    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default-user.png',
        blank=True,
    )
    website = models.URLField(default='', blank=True)
    bio = models.TextField(max_length=280, default='', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
    )

    @property
    def username(self):
        return self.user.username

    @username.setter
    def username(self, username):
        self.user.username = username

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, email):
        self.user.email = email

    @property
    def fullname(self):
        return self.user.get_full_name()

    @fullname.setter
    def fullname(self, fullname):
        first_name, last_name = fullname.split(' ', 1)
        self.user.first_name = first_name
        self.user.last_name = last_name

    def update_user(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self.user, name, value)
        self.user.save()

    def follow(self, profile):
        if not self.is_following(profile):
            self.following.add(profile)

    def unfollow(self, profile):
        if self.is_following(profile):
            self.following.remove(profile)

    def is_following(self, profile):
        return self.following.filter(user=profile.user).count() == 1

    @classmethod
    def get_profile(cls, username):
        return cls.objects.get(user__username=username)


class Image(models.Model):
    """User-uploaded images is represented by this model."""

    image = models.ImageField(upload_to='uploads/')
    caption = models.TextField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='images',
    )


class Like(models.Model):
    """Likes are tracked by this intermediary model.

    It maintains a relationship with both Image and Profile models.
    """

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='likes',
    )


class Comment(models.Model):
    """Comments are represented by this model.

    It maintains a relationship with both Image and Profile models.
    """

    comment = models.CharField(max_length=280)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='comments',
    )
