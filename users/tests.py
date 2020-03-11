from django.test import TestCase

from users.models import CustomUser

# Create your tests here.
class UserTestCase(TestCase):
    def test_user(self):
        user1 = CustomUser.objects.create_user("joe", "joe@example.com", "password")
        self.assertEqual(user1.email, "joe@example.com")