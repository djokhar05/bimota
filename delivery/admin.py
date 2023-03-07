from django.contrib import admin
from .models import Delivery

# Register your models here.
# https: // pypi.org/project/django-random-id-model/


class DeliveryAdmin(admin.ModelAdmin):
    exclude = ["id"]


admin.site.register(Delivery, DeliveryAdmin)
