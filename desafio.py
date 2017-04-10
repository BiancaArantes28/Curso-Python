# -*- coding: UTF-8 -*-

class Data():

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print '%d/%d/%d' % (self.dia,self.mes,self.ano)
		