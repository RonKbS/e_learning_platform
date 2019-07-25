from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

user = get_user_model()

class Course(models.Model):
    user = models.ForeignKey(to=user, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField()



class UserRatings(models.Model):
    user = models.OneToOneField(to=user, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    course = models.OneToOneField(to=Course, on_delete=models.CASCADE)
