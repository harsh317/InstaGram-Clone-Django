from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import urllib.request
import json
with urllib.request.urlopen("https://geolocation-db.com/json") as url:
    data = json.loads(url.read().decode())
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    locat = data['country_name']

    def __str__(self):
        return self.title