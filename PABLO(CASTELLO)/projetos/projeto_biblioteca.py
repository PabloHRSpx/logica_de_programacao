# Biblioteca

import tkinter as tk
from tkinter import messagebox
# CRIAÇÃO DA JANELA
def Encontrar_usuario():
    nome = nome_usuario.get()

    if nome == "":
        messagebox.showwarning("Digite seu nome: ")
    else:
        messagebox.showinfo("Bem-Vindo!", f"Olá {nome}. Seja bem vindo na biblioteca virtual!")

def segunda_janela():
    livro = livro_usuario.get()
    segunda_janela = tk.Toplevel(janela)
    segunda_janela.title("Segunda Janela")
    segunda_janela.geometry("500x300")

# CONFG. DA JANELA

janela = tk.Tk()
janela.title("Biblioteca Virtual")
janela.geometry("450x100")
janela.configure(bg="green")


# MENSAGEM
lbl_mensagem = tk.Label(janela, text="Digite o seu nome: ")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem2 = tk.Label(segunda_janela, text="Digite o nome do livro: ")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# RESPONDER
nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)

livro_usuario = tk.Entry(segunda_janela, font=("Arial", 12))

# BOTÕES
btn_mensagem = tk.Button(janela, text="Confirmar", command= Encontrar_usuario)
btn_mensagem.grid(row=0, column=2, pady=10, padx=10)

bnt_segunda_janela = tk.Button(janela, text= "Abrindo Segunda Janela", command=segunda_janela)
bnt_segunda_janela.grid(row=3, column=0, pady=10, padx=10)

bnt_segunda_janela = tk.Button(janela, text= "Abrindo Segunda Janela", command=segunda_janela)
bnt_segunda_janela.grid(row=3, column=0, pady=10, padx=10)





janela.mainloop()