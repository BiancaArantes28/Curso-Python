# -*- coding: UTF-8 -*-

class Imc():

	def __init__(self, peso, altura):
		self.peso = peso
		self.altura = altura

	def calculaImc(self):
		self.imc = self.peso / (self.altura * self.altura)
		print 'IMC = %f' % (self.imc)