from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max

# Create your models here.


class Term(models.Model):
    name = models.CharField(max_length=30, null = False)
    name = models.CharField(max_length=120, null = False)
    quantity =  models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)])