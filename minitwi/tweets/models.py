from django.db import models


class Tweet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tweets', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

