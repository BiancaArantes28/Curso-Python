# -*- coding: UTF-8 -*-

def cadastrar(nomes):
	print "Digite o nome"
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print "Listando nomes:"
	for nome in nomes:
		print nome

def remover(nomes):
	print "Qual nome vc deseja remover?"
	nome = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print 'Qual nome vc quer alterar'
	nome = raw_input()
	if(nome in nomes):
		posicao = nomes.index(nome)
		print 'Digite o nome nome'
		nome_novo = raw_input()
		nomes[posicao] = nome_novo

def procurar(nomes):
	print 'Digite o nome que procura'
	nome_a_procurar = raw_input()
	if(nome_a_procurar in nomes):
		print "O nome existe"
	else:
		print "O nome não exite"

def procurar_nomes(nomes):
	print 'Digite a expressão regular'
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	import re
	resultados = re.findall(regex,nomes_concatenados)
	print(resultados)

def menu():
	nomes = []
	escolhe = ''
	while(escolhe != '0'):
		print "Digite: 1 para cadastrar, 0 para terminar,2 para listar e 3 para remover, 4 para alterar, 5 para procurar, 6 procurar por nomes regulares"
		escolhe = raw_input()

		if(escolhe == '1'):
			cadastrar(nomes)

		if(escolhe == '2'):
			listar(nomes)

		if(escolhe == '3'):
			remover(nomes)

		if(escolhe == '4'):
			alterar(nomes)

		if(escolhe == '5'):
			procurar(nomes)

		if(escolhe == '6'):
			procurar_nomes(nomes)

menu()
