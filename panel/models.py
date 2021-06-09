from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from typing import Any, Dict


# Create your models here.
class Content(models.Model):
    title = models.CharField(
        max_length=152,
    )
    date_created = models.DateTimeField(
        # auto_now_add = True,
        default=timezone.now,
    )
    my_content = models.TextField(
        blank = False,
        verbose_name = 'Content of note'
    )
    author = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
    )
    image = models.ImageField(
        default='',
        upload_to='images',
        blank=True,
        null=True,
    )
    audio = models.FileField(
        default='',
        upload_to='audio',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})