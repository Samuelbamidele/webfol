from django.db import models

class AboutMe(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField()
    cv_link = models.FileField(upload_to='resumes/', blank=True, null=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    project_link = models.URLField(blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    link = models.URLField(max_length=300, blank=True, null=True)  # Field for an optional external link