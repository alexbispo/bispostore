# coding=utf-8

from django.test import TestCase, Client

from django.core.urlresolvers import reverse

from model_mommy import mommy


class ProductList(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.products = mommy.make('catalog.product', _quantity=10)
        self.client = Client()

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['products']
        self.assertEquals(product_list.count(), 10)


class CategoryTestCase(TestCase):

    def setUp(self):
        self.category = mommy.make('catalog.category', slug='acessorios')
        self.url = reverse('catalog:category', kwargs={'slug': self.category.slug})
        self.client = Client()
        self.products = mommy.make('catalog.product', category=self.category, _quantity=10)

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/category.html')

    def test_context(self):
        response = self.client.get(self.url)
        context = response.context
        category_products = context['category_products']

        self.assertTrue('current_category', 'category_products' in context)
        self.assertEquals(context['current_category'], self.category)
        self.assertEquals(category_products.count(), len(self.products))


class ProductTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make('catalog.product', slug='palheta-para-clarinete')
        self.url = reverse('catalog:product', kwargs={'slug': self.product.slug})
        self.client = Client()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product' in response.context)
        self.assertEquals(response.context['product'].id, self.product.id)
