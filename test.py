import unittest
from clipy_app import app
from db import session, Url
from utils import generar_url

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_post(self):
        url_original = 'https://www.example.com'
        response = self.app.post('/', data={'url_original': url_original})
        self.assertEqual(response.status_code, 200)
        self.assertIn(url_original, response.data.decode())

        url = session.query(Url).filter_by(url_original=url_original).first()
        self.assertIsNotNone(url)

    def test_redireccionar_url(self):
        url_original = 'https://www.example.com'
        url_recortada = generar_url()
        url = Url(url_original=url_original, url_recortada=url_recortada)
        session.add(url)
        session.commit()

        response = self.app.get('/{}'.format(url_recortada))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, url_original)

    def test_mostrar_urls(self):
        url_original = 'https://www.example.com'
        url_recortada = generar_url()
        url = Url(url_original=url_original, url_recortada=url_recortada)
        session.add(url)
        session.commit()

        response = self.app.get('/urls')
        self.assertEqual(response.status_code, 200)
        self.assertIn(url_original, response.data.decode())

if __name__ == '__main__':
    unittest.main()