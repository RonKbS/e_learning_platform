from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from api import constants

user = get_user_model()



class CourseCurriculumBaseClass(models.Model):
    user = models.ForeignKey(to=user, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField()

    class Meta:
        abstract = True

class CurriculumPackage(CourseCurriculumBaseClass):
    pass


class Course(CourseCurriculumBaseClass):
    curriculum_package = models.ForeignKey(
        to=CurriculumPackage, on_delete=models.CASCADE, null=True, blank=True
    )


class CourseRating(models.Model):
    user = models.OneToOneField(to=user, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    course = models.OneToOneField(to=Course, on_delete=models.CASCADE)


class CourseContent(models.Model):
    name = models.CharField(unique=True, max_length=50)
    content_type = models.CharField(
        max_length=50,
        choices=constants.content_type,
    )
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    course_media = models.FileField(
        upload_to='course_media/', null=True, verbose_name=""
    )


# for a student to enroll to a curriculum package
# it should be a many-to-many field