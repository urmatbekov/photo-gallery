from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images")
    alt = models.CharField(max_length=240,null=True,blank=True)
    title = models.CharField(max_length=240)
    description = models.TextField()

    def __str__(self):
        return self.title