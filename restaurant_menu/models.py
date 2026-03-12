from django.db import models


MEAL_TYPE = (
        ("starters", "Starters"),
        ("salads", "Salads"),
        ("main_dishes", "Main_dishes"),
        ("desserts", "Desserts"),
)

# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=100)

