from django.contrib.auth import get_user_model

from ships.tests import BaseTestCase

User = get_user_model()


class ShipsAdminTest(BaseTestCase):
    def test_admin_game(self):
        self.client.login(username=self.username, password=self.password)
        resp = self.client.get("/admin/ships/ship/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "admin/base.html")

        resp = self.client.get("/admin/ships/ship/add/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "admin/change_form.html")
