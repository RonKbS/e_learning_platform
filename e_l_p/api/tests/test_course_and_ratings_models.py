from django.test import TestCase

from api.models.users import User
from api.models.courses import Course, CourseRating

class CourseModelTestCase(TestCase):
    """Test that a course can be created"""

    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
            email="test_user@gmail.com",
        )
        self.course = Course.objects.create(
            user=self.user,
            name="Javascript",
            description="This is a Javascript basics course",
        )

    def test_a_course_can_be_created(self):
        count = Course.objects.count()
        Course.objects.create(
            user=self.user,
            name="Python",
            description="This is a python basics course",
        )
        self.assertEqual(Course.objects.count(), count + 1)

    def test_a_user_rating_can_be_created(self):
        self.user_1 = User.objects.create(
            username="test_user_1",
            email="test_user_1@gmail.com",
        )
        count = CourseRating.objects.count()
        CourseRating.objects.create(
            user=self.user_1,
            rating=5,
            course=self.course,
        )
        self.assertEqual(CourseRating.objects.count(), count + 1)
