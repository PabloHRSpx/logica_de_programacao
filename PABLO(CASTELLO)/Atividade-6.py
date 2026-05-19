#Clean Code - Aula 6
#Para que usar?
#como usar?
#print("Clean Code - Aula 6")
#Aula = 6
#print(f"Estamos na aula (aula) de Clean Code")

# texto = " Python é muito legal! "

# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split()) # ["Python"]

# # Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code.")

# # Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:
# Crie um programa que peça ao usúario para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - Remova os espaços extras no início e no final da frase.

# texto = input("Qual é sua frase? ")
# print(texto.strip().replace(" ", ""))

# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de um texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o resultado para o usúario

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras é {contagem}")

# Execução de comandos do sistema
import os # Importa o módulo os para interagir com o sistema operacional
# # onde estou?
# print(os.getcwd())
# # Lista arquivos na pasta
# print(os.listdir()) 
# print(os.listdir("..")) # Lista arquivos da pasta pai
# print(os.listdir("..\\..")) # Lista arquivos da pasta avô
# print(os.listdir("C:\\")) # Lista arquivos da raiz do C
# print(os.listdir("C:\\Users"))# Lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Public")) # Lista arquivos da pasta public

# Outros comandos úteis:
# # Criar pasta
# os.mkdir("nova_p.readasta")
# # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercicio 2:
# Cria um script que mostra o caminho da pasta atual.
# print(os.getcwd())
# Exercicio 3:
# Liste os arquivos da pasta atual
# print(os.listdir())
# Exercicio 4:
# Crie uma pasta chamada "projeto" e depois renomeia para "meus_projetos". Por fim, exclua a pasta.
# os.mkdir("projeto")
# os.rename("meus_projetos")
# os.rmdir("meus_projetos")

# Exercicio 5:
# Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Despois, leia o conteúdo do arquivo e exiba na tela.
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")
# with open("Log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemplo de dicionario:
# Cria um dicionario com informações sobre uma pessoa e acesse um valor usando uma chave.

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "Profissão": "Engenheiro"   
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Designer"
# }
# print(pessoa["cidade"])
# print(pessoa2["nome"], pessoa["idade"])

# Exemplo 2: Desligar o PC (comando para windows)
with open("desligar.txt", "a") as desligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")
    # -s comando para desligar
    # -t tempo definir
    # -a cancelar desligamento

# with open("desliga.bat", "r") as desligar: