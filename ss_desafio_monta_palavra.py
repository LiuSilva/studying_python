#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Desafio Processo Seletivo Studio Sol - 03/11/2017

Montar Palavras

Lógica: Depois que o usuario inserir as letras disponíveis, o banco de palavras
        vai ser percorrido procurando palavras que estejam no banco de dados e 
        possuam todas as letras que foram informadas pelo usuario.
        Assim quando todas as letras da palavra do banco de palavras existirem
        na lista que o usuario informou, é porque é possível formar aquela palavra,
        assim essa palavra é inserida em uma lista de palavras que deram match com
        as letras informadas pelo usuario. Após é feito a verificacao de qual é a
        palavra que gera a maior pontuacao.
@author: Luciano Silva
"""

valor_letras = {
    'e': 1,
    'a': 1,
    'i': 1,
    'o': 1,
    'n': 1,
    'r': 1,
    't': 1,
    'l': 1,
    's': 1,
    'u': 1,
    'w': 2,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10,
}

banco_palavras = ("abacaxi", "manada", "mandar", "porta", "mesa",
                  "dado", "mangas", "ja", "coisas", "radiografia",
                  "matematica", "drogas", "predios", "implementacao", "computador",
                  "balao", "xicara", "tedio", "faixa", "livro", "deixar", "superior"
                  "profissao", "reuniao", "montanha", "botanica", "banheiro", "caixas"
                  "xingamento", "infestacao", "cupim", "premiada", "empanada",
                  "ratos", "ruido", "antecedente", "empresa", "emissario", "folga",
                  "fratura", "goiaba", "gratuito", "hidrico", "homem", "jantar",
                  "jogos", "montagem", "manual", "nuvem", "neve", "operacao",
                  "ontem", "pato", "pe", "viagem", "queijo", "quarto", "quintal",
                  "solto", "rota", "selva", "tatuagem", "tigre", "uva", "ultimo",
                  "virtuperio", "voltagem", "zangado", "zombaria", "dor", "batata")

palavras_input = input('​Digite​ as letras​ disponíveis nesta​ jogada: ')
palavras_input = palavras_input.strip().lower()
letras_disponiveis = [i for i in palavras_input]

# cada palavra do banco de palavras e decomposta em um conjunto de letras
# cada letra do conjunto de letras formado em cada iteracao é verificado
# se existe a letra conjunto de letras disponiveis informadas pelo usurio, 
# se todas as letras da palavra do banco de dados existem no conjunto deu match!
matches = []

for palavra in banco_palavras:
    letras_palavra = [i for i in palavra]
    
    match = True
    letras_possiveis = letras_disponiveis[:]
    for letra in letras_palavra:
        if letra not in letras_possiveis:
            match = False
        else:
            letras_possiveis.remove(letra)
    
    if match:
        matches.append(palavra)

# confere qual e a palavra de maior pontuacao possivel
maior_pontuacao = 0
palavra_maior_pontuacao = ''

for palavra in matches:
    pontuacao = 0
    
    for p in palavra:
        pontuacao += valor_letras[p]
    
    if pontuacao > maior_pontuacao:
        maior_pontuacao = pontuacao
        palavra_maior_pontuacao = palavra
    elif pontuacao == maior_pontuacao:
        if len(palavra_maior_pontuacao) > len(palavra):
            maior_pontuacao = pontuacao
            palavra_maior_pontuacao = palavra

if palavra_maior_pontuacao:
    print(palavra_maior_pontuacao.upper() + ", palavra de", maior_pontuacao, "pontos")
    
    # letras que sobraram
    letras_sobraram = []
    
    for p in letras_disponiveis:
        if p not in palavra_maior_pontuacao:
            letras_sobraram.append(p)
    
    print("Sobraram:", end=" ")
    for s in letras_sobraram:
        print(s.upper(), end=" ")
    print()
else:
    print("Não foi possível formar uma palavra usando as letras disponíveis:", palavras_input)