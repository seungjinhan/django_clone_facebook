from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel


class Photo(TimeStampedModel):

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey(
        "Post", related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Post(TimeStampedModel):

    OPEN_NOT = "not"
    OPEN_FRIEND = "friends"
    OPEN_ALL = "all"
    OPEN_CHOICES = (
        (OPEN_NOT, _("Not")),
        (OPEN_FRIEND, _("Friends")),
        (OPEN_ALL, _("All")),
    )

    content = models.TextField()
    user = models.ForeignKey(
        'users.User',
        related_name='post',
        on_delete=models.CASCADE
    )
    open = models.CharField(
        _("open"),
        choices=OPEN_CHOICES,
        max_length=10,
        blank=False,
        default=OPEN_ALL
    )

    def __str__(self):
        return self.content[:20]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
