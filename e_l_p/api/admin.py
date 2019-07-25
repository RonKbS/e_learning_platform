from django.contrib import admin

from .models.users import User
from .models.courses import Course, UserRatings

admin.site.register(
    [User, Course, UserRatings]
)
