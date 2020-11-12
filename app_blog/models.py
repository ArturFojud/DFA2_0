#import potrzebnych modulow

from django.db import models
from django.utils import timezone

#Utworzenie modelu Wpisu na bloga - 'Post' - to przyjęta nazwa model

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# definicja metody 'publish' - czyli publikującej wpis

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
