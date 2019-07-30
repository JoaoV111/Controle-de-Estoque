# -*- coding: utf-8 -*-
'''Testes automatizados.
	Docs: https://docs.pytest.org/en/latest/contents.html
	To run all test use this commands on bash 'pytest tests.py'
'''
import unittest
from unittest.mock import patch
from useful import setup_db, Product, _searchProduct

# Iniciando conexão ao banco de dados
setup_db()

class ControleEstoqueTestCase(unittest.TestCase):
	def test_product_definition(self):
		product = Product(name='name_test', model='model_test', quantity=7)

		self.assertEqual(product.name, 'name_test')
		self.assertEqual(product.model, 'model_test')
		self.assertEqual(product.quantity, 7)

class test_searchProduct(unittest.TestCase):
	@patch('_searchProduct().get_input', return_value='pd001')
	def test_pd001(self, input):
		instance = _searchProduct()
		self.assertEqual(instance[0], Product(id='1', name='Presunto', model='Perdigão', quantity='50'))

	@patch('_searchProduct().get_input', return_value='pd999')
	def test_searchProduct_fail(self, input):
		self.assertEqual(_searchProduct(), [])

