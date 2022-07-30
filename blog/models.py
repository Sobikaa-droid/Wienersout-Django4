from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=40)
    # url = models.URLField(blank=True)  # 'blank=true' if some urls want to be not clickable
    date = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self):  # show project name in admin page instead of 'Project (1)'
        return self.title
