# Tratamento de Erros
# Organizar de forma adequada o código é essencial para evitar erros e garantir que o programa funcione corretamente. O tratamento de erros é uma prática importante para lidar com situações inesperadas que podem ocorrer durante a execução do programa.

# try e except são estruturas usadas para capturar e lidar com erros de forma controlada. O código dentro do bloco try é excecutado normalmente, mas se ocorrer um erro, o programa pula para o bloco except, onde você pode definir como lidar com o erro.

# Erros comuns:
# - ZeroDIvisionError: divisão por zero
# - ValueError: conversão de tipo inválida
# - IndexError: acesso a índice fora do limite
# - KeyError: acesso a chave inexistente em dicionário

# try:
#     numero = int(input("Digite um numero: "))
#     resultado = 10 / numero
#     print(f"O resultado é: {resultado}")

#     except ValueError: 
#     print("Erro: Você deve digitar um número válido.")
        
# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero.")
        
# except Exception as erro:
#     print(f"Ocorreu um erro inesperado: {erro}")
#     break

# print("Programa encerrado.")

# Exercicio 1:
#Crie um algoritmo para calcular a média e trate o erro ao inserir valores errados.

# try:
#     numero = int(input("Digite o numero:"))
#     numero2 = int(input("Digite o segundo numero:"))
#     total = numero + numero2
#     print(f"O resultado é: {total/2}")

# except ValueError:
#     print("Erro: você digitou um numero incorreto")

# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número inteiro.
# - ZeroDivisionError: se a lista de números estiver vazia.

# len: Retorna o número de itens de um objeto. Pode ser usado para obter o comprimento de uma string, lista, dicionário, etc.
# append: Adiciona um item ao final de uma lista.

# print("Calcularoda de média em lista")

# try:
#     numero = int(input("Digite um número inteiro para definir o tamanho da lista:"))
#     lista = []
#     for listagem in range(numero):
#         numero_lista = float(input(f"Digite o número {listagem + 1}:"))
#         lista.append(numero_lista)

#     media = sum(lista) / len(lista)
#     print(f"A média dos números é: {media}")
#     break
# except ValueError:
#     print("Erro: Você deve digitar um número inteiro válido. Tente novamente.")
#     break
# except ZeroDivisionError:
#     print("Erro: A lista de números está vazia. Não é possivel calcular a média.")
#     break
# print("Programa encerrado.")

# Exercicio 3:
# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um string.

try:
    palavras = input("Digite uma lista de palavras separadas por espaço").split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    print("COntagem de palavras.")
    for palavra, contagem in contagem.items():
        print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada Inválida: Digite uma lista separada por espaços")