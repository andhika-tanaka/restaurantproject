from django.conf import settings
from django.db import models
from django.utils import timezone

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    main_ingredient = models.CharField(max_length=300)
    description = models.CharField(max_length=300)     
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
