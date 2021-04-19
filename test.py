import unittest
from flask import json
from flask.testing import FlaskClient

import timezones

class FlaskTimezonesTests(unittest.TestCase):

    # Préparation du client de test avec lequel nous allons interagir
    def setUp(self):
        self.app = timezones.create_app().test_client()
    
    def test_context_exists(self):
        self.assertIsInstance(self.app, FlaskClient)

    def test_i_m_lost(self):
        resp = self.app.delete("/je/suis/perdu")
        self.assertEqual(resp.status_code, 404)
    
    # TESTS api/gmt

    def test_gmt_status_200(self):
        resp = self.app.get("/api/gmt/+0")
        self.assertEqual(resp.status_code, 200)
    
    def test_gmt_response_has_timezone(self):
        resp = self.app.get("/api/gmt/-1")
        data = json.loads(resp.data)

        self.assertTrue("timezone" in data)
    
    def test_gmt_response_has_time(self):
        resp = self.app.get("/api/gmt/-1")
        data = json.loads(resp.data)

        self.assertTrue("time" in data)
    
    def test_gmt_response_has_hour(self):
        resp = self.app.get("/api/gmt/-7")
        data = json.loads(resp.data)

        self.assertTrue("hour" in data)

    def test_gmt_response_has_date(self):
        resp = self.app.get("/api/gmt/+3")
        data = json.loads(resp.data)

        self.assertTrue("date" in data)

    def test_gmt_response_has_locales(self):
        resp = self.app.get("/api/gmt/-4")
        data = json.loads(resp.data)

        self.assertTrue("locales" in data)

    def test_gmt_response_hour_has_hour(self):
        resp = self.app.get("/api/gmt/+10")
        data = json.loads(resp.data)

        self.assertTrue("hour" in data["hour"])
