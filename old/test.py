from old.Main import generar_url
import unittest

class TestGenerarUrl(unittest.TestCase):
    def test_generar_url(self):
        url = generar_url()
        self.assertEqual(len(url), 6)
        self.assertIsInstance(url, str)
