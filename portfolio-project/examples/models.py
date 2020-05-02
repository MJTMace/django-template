from django.db import models
import os
from django.conf import settings

# Create your models here.


class Example(models.Model):
    # Image (illustrative picture):
    image = models.ImageField(upload_to="images/")
    # Summary (text explanation):
    summary = models.CharField(max_length=200)

    # Other images for the individual example's detail page:
    imagedetail1 = models.ImageField(
        upload_to="images/",
        default=os.path.join(settings.STATIC_ROOT, "images", "photo_MM.jpg"),
    )
    imagedetail2 = models.ImageField(
        upload_to="images/",
        default=os.path.join(settings.STATIC_ROOT, "images", "photo_MM.jpg"),
    )
    # More detailed text summary:
    summarydetail = models.CharField(max_length=1500, default="")

    # Display example summary in Django admin instead of 1,2,3...
    def __str__(self):
        return self.summary
