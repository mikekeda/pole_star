from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class BaseTestCase(TestCase):
    username = "testadmin"
    password = "12345"
    test_admin = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create admin user.
        cls.test_admin = User.objects.create_superuser(
            username=cls.username,
            email="myemail@test.com",
            password=cls.password,
            first_name="Bob",
            last_name="Smit",
        )
        cls.test_admin.save()
