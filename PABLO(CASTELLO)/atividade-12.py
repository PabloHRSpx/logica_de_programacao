# Interface Gráfica
# Componentes Principais (Widgets)

# tk: Janela principal
# label: Texto ou rotulo
# Button: Um botão clicável 
# Entry: Um campo deentrada de texto

import tkinter as tk
from tkinter import messagebox

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela GUI")
janela.geometry("400x200") #Largura X Altura

# 2. Criar a função que o botão irá executar 
def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão :)")

# 3. Criar os componentes
lbl_titulo_janela = tk.Label(janela, text="Bem vindo a aula de Interface Gráfica!\n Aula 12 - Interface Gráfica", font=("Arial", 14, "bold"))
btn_clique_janela = tk.Button(janela, text="Clique Aqui", font=("Arial", 14), bg="#B68989", fg="black", command=mostrar_mensagem)

# 4. Posicionar os componentes na janela
lbl_titulo_janela.pack(pady=20) #pady adiciona um espaçamento vertical
btn_clique_janela.pack(pady=15)

# # 5. Rodar o loop da interface
janela.mainloop()