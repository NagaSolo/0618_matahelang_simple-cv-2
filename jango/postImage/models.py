from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

class PostImage(models.Model):
    title = models.TextField()
    content = models.TextField()
    cover = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # membolehkan django membaca string url
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={ 'pk' : self.pk })