from django.db import models
from ckeditor.fields import RichTextField
from thumbnails.fields import ImageField
# Create your models here.

CLOTH_CATEGORY_OPTIONS = (
    ("top", "Top"),
    ("bottom", "Bottom"),
    ("complete", "Complete"),
)
CLOTH_GENDER_OPTIONS = (
    ("male", "Male"),
    ("female", "Female"),
    ("unisex", "Unisex"),
)


class Clothe(models.Model):
    cloth_name = models.CharField(max_length=50, unique=True)
    # cloth_image = models.CharField(max_length=300)
    cloth_image = models.ImageField(upload_to="images", default="default.jpg")
    cloth_thumbnail = ImageField(
        upload_to='images', default='default.jpg', resize_source_to="large")
    cloth_category = models.CharField(
        max_length=8, choices=CLOTH_CATEGORY_OPTIONS, default='top')
    cloth_gender = models.CharField(
        max_length=8, choices=CLOTH_GENDER_OPTIONS, default='male')
    cloth_price = models.FloatField()
    cloth_description = RichTextField()
    slug = models.SlugField(default='', editable=False,
                            max_length=200, null=False)
