from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.name} | {self.rating} | {self.review}"