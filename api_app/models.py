from django.db import models


class JokeModel(models.Model):
    topic_input = models.TextField()
    text_joke = models.TextField()

    def __str__(self):
        return self.text_joke[:30]


