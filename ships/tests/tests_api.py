from rest_framework.test import APITestCase

from ships.tests import BaseTestCase


class ShipsApiTest(BaseTestCase, APITestCase):
    def test_ships_api(self):
        """ Test /api/ships api. """
        self.client.force_authenticate(self.test_admin)

        resp = self.client.get("/api/ships/")
        self.assertEqual(resp.status_code, 200)
        ships = resp.json()
        self.assertEquals(len(ships), 3)
        self.assertTrue("imo" in ships[0].keys())
        self.assertTrue("name" in ships[0].keys())

    def test_locations_api(self):
        """ Test /api/positions api. """
        self.client.force_authenticate(self.test_admin)

        resp = self.client.get("/api/positions/9247455/")
        self.assertEqual(resp.status_code, 200)
        positions = resp.json()
        self.assertTrue(len(positions) > 0)
        self.assertTrue("latitude" in positions[0].keys())
        self.assertTrue("longitude" in positions[0].keys())
