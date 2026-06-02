import tkinter as tk
from tkinter import messagebox

# .get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()
    idade = idade_usuario.get()
    if nome == "" and idade -- "":
        messagebox.showwarning("Aviso", "Digite seu nome :)")
    else:
        messagebox.showinfo("Bem-vindo", f"Olá usuário {nome}, e você tem {idade} anos - Seja bem-vindo no nosso sistema")
   

    # Janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="pink")

    # Componentes
lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_idade = tk.Label(janela, text="Digite a sua idade :)") 
lbl_idade.grid(row=1, column=0, pady=10, padx=10)


nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)

idade_usuario = tk.Entry(janela, font=("Arial", 12))
idade_usuario.grid(row=1, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

    # Rodar interface
janela.mainloop()