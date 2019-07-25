from django.contrib import admin

from .models.users import User
from .models.courses import Course, CourseRating, CourseContent

admin.site.register(
    [User, Course, CourseRating, CourseContent]
)
