from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CheckConstraint, Q
from django.db.models.functions import Lower


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'  # переопределение поля кастомного юзера
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(unique=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(email=Lower("email")), name="user_email_lower"),
        ]


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
