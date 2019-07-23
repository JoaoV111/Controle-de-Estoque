# -*- coding: utf-8 -*-
'''Testes automatizados.
	Docs: https://docs.pytest.org/en/latest/contents.html
	To run all test use this commands on bash 'pytest tests.py'
'''
import unittest

from config import Product

class ControleEstoqueTestCase(unittest.TestCase):
	def test_product_definition(self):
		product = Product('name_test', 'model_test', 7)

		self.assertEqual(product.name, 'name_test')
		self.assertEqual(product.model, 'model_test')
		self.assertEqual(product.qt, 7)
