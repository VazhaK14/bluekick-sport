from django.test import TestCase, Client
from .models import Product

# Create your tests here.
class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_news_creation(self):
        product = Product.objects.create(
          name='Premium Football',
          price=500000,
          stock=5,
          description='Limited hand made football!',
          category='ball',
        )

        self.assertTrue(product.is_avail)
        self.assertFalse(product.is_product_top)
        product.give_rating(4)
        self.assertTrue(product.is_product_top)

    def test_invalid_rating(self):
        product = Product.objects.create(
          name='Premium Football',
          price=500000,
          stock=5,
          description='Limited hand made football!',
          category='ball',
        )

        with self.assertRaises(ValueError) as e:
            product.give_rating(999) 
        
        self.assertEqual(str(e.exception), 'Rating Product is 0-5')