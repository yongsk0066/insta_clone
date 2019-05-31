from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    #
    # GENDER_CHOICES = (
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('not-specified', 'Not specified')
    # )
    #
    # name = models.CharField(blank=True, max_length=255)
    # website = models.URLField(null=True)
    # bio = models.TextField(null=True)
    # phone = models.CharField(max_length=140, null=True)
    # gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})