from splinter import Browser
from time import sleep
from models import Amigo
import unittest
import json
import urllib2


class TestController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('firefox')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test01_get_amigos(self):
        self.browser.visit("http://localhost:8000/amigos")
        self.assertEqual(self.browser.status_code.code, 200)
        self.assertTrue(self.browser.is_text_present('{"amigos": []}'))

    def test02_post_amigos(self):
        data = {"amigos":[{"latitude":1, "longitude":2, "nome":"rocha"}]}
        req = urllib2.Request("http://localhost:8000/amigos")
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(data))
        self.assertEquals(response.read(), 'Amigo(s) adicionado(s)')

    def test03_get_amigo_id(self):
        self.browser.visit("http://localhost:8000/amigos?id=1")
        self.assertEqual(self.browser.status_code.code, 200)
        self.assertTrue(self.browser.is_text_present('{"amigo": {"latitude": 1, "id": 1, "longitude": 2, "nome": "rocha"}}'))

    def test04_post_vector_amigos(self):
        data = {"amigos": [{"latitude":1, "longitude":3, "nome":"2"},
                           {"latitude":1, "longitude":4, "nome":"3"},
                           {"latitude":3, "longitude":1, "nome":"4"},
                           {"latitude":2, "longitude":2, "nome":"5"}]}
        req = urllib2.Request("http://localhost:8000/amigos")
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(data))
        self.assertEquals(response.read(), 'Amigo(s) adicionado(s)')

    def test05_get_amigos_proximos(self):
        self.browser.visit("http://localhost:8000/amigos_proximos/?id=1")
        self.assertEqual(self.browser.status_code.code, 200)
        self.assertTrue(self.browser.is_text_present('{"amigos": [{"latitude": 1, "id": 2, "longitude": 3, "nome": "2"}'))
        self.assertTrue(self.browser.is_text_present('{"latitude": 2, "id": 5, "longitude": 2, "nome": "5"}'))
        self.assertTrue(self.browser.is_text_present('{"latitude": 1, "id": 3, "longitude": 4, "nome": "3"}]}'))

    def test06_get_amigos_proximos_sem_id(self):
        self.browser.visit("http://localhost:8000/amigos_proximos")
        self.assertEqual(self.browser.status_code.code, 200)
        self.assertTrue(self.browser.is_text_present("Informe o id do amigo a ser analisado"))

if __name__ == "__main__":
    unittest.main()