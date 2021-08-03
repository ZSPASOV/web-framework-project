from django.test import TestCase
from .models import FavouriteProduct
from django.contrib.auth.models import User
from products.models import Product
from django.urls import reverse


# Create your tests here.


class FavouriteProductTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_user("test_user," "test@gmail.com", "test123")
        cls.product=Product.objects.create(name="testing product",image='/', description='cool',price=20.3)

    def test_favorite_entry(self):
        imgpath = 'media/product_img/apple.jpg'
        entry = FavouriteProduct.objects.create(product=self.product ,user=self.user, is_favourite=False)
        res = 'product {} {} by {}'.format('testing product', 'marked favourite', '')
        self.assertEqual(str(entry),res)

    def test_with_authenticate_user_favourite(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse('mark-favourite',kwargs={'id':self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('marked' in response.json())
        self.assertTrue(response.json()['marked'])

    def test_with_unauthenticate_user_favourite(self):
        with self.assertRaises(TypeError):
            response = self.client.get(reverse('mark-favourite',kwargs={'id':self.product.id}))
        