from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductModelTest(TestCase):

    def test_one_entry(self):
        imgpath = 'media/product_img/apple.jpg'
        entry = Product.objects.create(name="testing product",image=imgpath, description='cool',price=20.3)
        self.assertEqual(str(entry),'testing product')


    def test_with_empty_data(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create()

    def test_with_exceeded_price(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create(name="testing product",image=imgpath, description='cool',price=2000000000.3)


    def test_with_empty_name(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create(image=imgpath, description='cool',price=2000000000.3)


    def test_with_empty_description(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create(image=imgpath, name="testing product", price=2000000000.3)


    def test_with_empty_image(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create(name="testing product", description='cool',price=2000000000.3)


    def test_with_empty_price(self):
        with self.assertRaises(Exception):
            imgpath = 'media/product_img/apple.jpg'
            entry = Product.objects.create(image=imgpath, description='cool',name="testing product")
