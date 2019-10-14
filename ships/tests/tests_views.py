from ships.tests import BaseTestCase


class ShipsViewTest(BaseTestCase):
    def test_views_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")
