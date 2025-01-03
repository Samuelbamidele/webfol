from django.db import models
class About(models.Model):
    content = models.TextField(help_text="Details about yourself")
    image = models.ImageField(upload_to='about/', null=True, blank=True, help_text="Upload an image of yourself")
    cv = models.FileField(upload_to='cv/', null=True, blank=True, help_text="Upload your CV")

    def __str__(self):
        return "About Me"

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