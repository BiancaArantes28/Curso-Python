# -*- coding: UTF-8 -*- 

class Perfil():
	'Classe para padrao perfis de usuario'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprimir(self):
		print 'Nome: %s, Telfone %s, Empresa %s' % (self.nome,self.telefone,self.empresa)