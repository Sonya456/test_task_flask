import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Kalendarz Wydarzeń', response.data.decode('utf-8'))

    def test_event_detail(self):
        response = self.app.get('/event/1') 
        self.assertEqual(response.status_code, 200)
        self.assertIn('Opis:', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
