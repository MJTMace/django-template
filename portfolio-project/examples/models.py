from django.db import models

# Create your models here.


class Example(models.Model):
    # Image (illustrative picture):
    image = models.ImageField(upload_to="images/")
    # Summary (text explanation):
    summary = models.CharField(max_length=200)
