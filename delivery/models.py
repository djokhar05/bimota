from django.db import models
from ckeditor.fields import RichTextField
from django_random_id_model import RandomIDModel
from django.urls import reverse


DELIVERED_OPTIONS = (
    ("false", "Not Delivered"),
    ("true", "Delivered"),
)


# Create your models here.
class Delivery(RandomIDModel):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    measurements = RichTextField(default='')
    items = models.CharField(max_length=200, default='', blank=True)
    delivered = models.CharField(
        max_length=200, choices=DELIVERED_OPTIONS, default="false")

    def get_absolute_url(self):
        return reverse("order_complete", kwargs={"pk": self.pk})
