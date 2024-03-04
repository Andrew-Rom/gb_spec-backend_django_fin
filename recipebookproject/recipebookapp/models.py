from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Recipe(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.PositiveIntegerField()
    image = models.ImageField(null=True, upload_to='recipes/', blank=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    entry_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
