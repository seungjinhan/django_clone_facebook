from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy
from django.db import models

from core.models import TimeStampedModel


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    about_me = models.CharField(max_length=255)

    login_method = models.CharField(
        gettext_lazy("login_method"),
        choices=LOGIN_CHOICES,
        max_length=50,
        default=LOGIN_EMAIL)

    hobbies = models.ManyToManyField(
        "users.Hobby",
        related_name="user",
        blank=True
    )

    def __str__(self):
        return self.email


class Friends(TimeStampedModel):
    me = models.ForeignKey(
        "users.User",
        related_name="friends_me",
        on_delete=models.CASCADE,
        unique=True

    )
    friend = models.ManyToManyField(
        "users.User",
        related_name="friends_friend",
        blank=False
    )
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return str(self.me)

    def count_friend_me(self):
        return Friends.objects.filter(
            friend=self.me
        ).count()
    count_friend_me.short_description = "나를 친구로 추가한 수"


class Hobby(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
