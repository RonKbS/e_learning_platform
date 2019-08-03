from django.test import TestCase

from api.models.users import User

class UserModelTestCase(TestCase):
    """ Test that a user can be created """

    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
            email="test_user@gmail.com",
        )


    def test_a_user_can_be_created(self):
        count = User.objects.count()
        User.objects.create(
            username="test_user1",
            email="test_user1@gmail.com",
        )
        self.assertEqual(User.objects.count(), count + 1)

    def test_a_user_can_be_made_staff_or_student(self):
        self.assertEqual(self.user.is_staff, False)
        self.user.is_staff = True
        self.assertEqual(self.user.is_staff, True)

        self.assertEqual(self.user.is_student, False)
        self.user.is_student = True
        self.assertEqual(self.user.is_student, True)
