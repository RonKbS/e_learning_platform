import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from api.models.users import User
from api.models.courses import Course, CourseRating, CourseContent

class CourseModelTestCase(TestCase):
    """Test that a course can be created"""

    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
            email="test_user@gmail.com",
        )
        self.user_1 = User.objects.create(
            username="test_user_1",
            email="test_user_1@gmail.com",
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
        count = CourseRating.objects.count()
        CourseRating.objects.create(
            user=self.user_1,
            rating=5,
            course=self.course,
        )
        self.assertEqual(CourseRating.objects.count(), count + 1)

    def test_course_content_can_be_created(self):
        count = CourseContent.objects.count()
        CourseContent.objects.create(
            name="python_course_content",
            content_type="video",
            course=self.course,
            course_media=SimpleUploadedFile(
                "file.pdf", b"file_content", content_type="document/pdf"
            )
        )
        self.assertEqual(CourseContent.objects.count(), count + 1)
        os.remove("media/course_media/file.pdf")
