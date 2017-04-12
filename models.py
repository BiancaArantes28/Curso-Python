# -*- coding: UTF-8 -*- 

class Perfil(object):
	'Classe para padrao perfis de usuario'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telfone %s, Empresa %s, Curtidas: %s' % (self.nome,self.telefone,self.empresa,self__curtidas)
		
	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

class Perfil_Vip(Perfil):
	'Classe para padrao perfis de usuario'

	def obter_creditos(self):
		return super(Perfil_Vip).__curtidas * 10