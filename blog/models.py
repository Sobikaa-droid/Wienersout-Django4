from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField(blank=True)  # 'blank=true' if some urls want to be not clickable
    date = models.DateField()
    description = models.TextField(max_length=140)
