# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
num = list(range(1,11))
for n in num:
    print(n ** 2)
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
list = ["Python", "Java", "C++", "JavaScript"]
list.remove("C++")
list.append("Ruby")
print(list)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for c, v in livro.items():
    print(f"{c}: {v}")
    
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
palavra = input("Digite uma palavra: ").lower()
contagem = {}
for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra]=1
print(contagem)

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos.values())
print(f"O valor para a lista de compras é total é {total}")
