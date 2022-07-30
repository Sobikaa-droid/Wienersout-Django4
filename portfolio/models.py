from django.db import models
# models need to be migrated into the database!


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # 'blank=true' if some urls want to be not clickable

    def __str__(self):  # show project name in admin page instead of 'Project (1)'
        return self.title
