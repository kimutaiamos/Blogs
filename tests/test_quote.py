import unittest
from app.models import Quote


class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        set up method that will run bfre every test
        """
        self.random_quote = Quote("sir amos kimutai", "Juice world forever")


        def test_instance(self):
            self.assertTrue(isinstance(self.random_quote, Quote))



        def test_init(self):
            self.assertEqual(self.random_quote.author, "amos")
            self.assertEqual(self.random_quote.quote,"life is good")