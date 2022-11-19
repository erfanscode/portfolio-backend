from django.db import models
from django.utils.html import format_html

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to="covers/", blank=True)
    video = models.FileField(upload_to="covers/", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def image_tag(self):
        try:
            return format_html("<img width=100 height=75 src='{}'>".format(self.image.url))
        except:
            pass
    image_tag.short_description = "image"

    def short_description(self):
        return str(self.description)[:50]
    short_description.short_description = "description"
