from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
from users.models import Profile


class Review(models.Model):  # new
    profile = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='reviews')
    review_author = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, related_name='author_submitted_reviews')
    review_text = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]) # https://stackoverflow.com/a/12026867/11576212


    def __str__(self):
        return self.review_text
