# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()
#     if nome == "" and turno -- "":
#         messagebox.showwarning("Aviso", "Digite seu nome :)")
#     else:
#         messagebox.showinfo("Bem-vindo", f"Operador {nome} registrado no turno {turno}. Boa jornada!")
   
#     # Janela
# janela = tk.Tk()
# janela.title("Operador e Turno")
# janela.geometry("300x300")
# janela.configure(bg="black")

#     # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite seu nome: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Digite seu turno: ") 
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)

# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()


# ATIVIDADE 2

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():

#     numero1 = int(numero_usuario.get())
#     numero2 = int(pecas_usuario.get())
#     resultado = numero1 * numero2

#     if  numero1 == "" and numero2 -- "" and resultado == "":
#         messagebox.showwarning("Digite a quantidade de peças: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"A quantidade de peças é de: {resultado}")
   

#     # Janela
# janela = tk.Tk()
# janela.title("Peças")
# janela.geometry("300x300")
# janela.configure(bg="black")

#     # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a quantidade de peças: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_horas = tk.Label(janela, text="Digite a quantidade de horas: ") 
# lbl_horas.grid(row=1, column=0, pady=10, padx=10)


# numero_usuario = tk.Entry(janela, font=("Arial", 12))
# numero_usuario.grid(row=0, column=1, pady=10, padx=10)

# pecas_usuario = tk.Entry(janela, font=("Arial", 12))
# pecas_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 3

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():

#     numero1 = float(bar_usuario.get())
#     numero2 = float(psi_usuario.get())
#     resultado = numero1 * numero2

#     if  numero1 == "" and numero2 -- "" and resultado == "":
#         messagebox.showwarning("Digite a quantidade de peças: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"A quantidade de Bar é: {resultado}")
   

#     # Janela
# janela = tk.Tk()
# janela.title("Calculo")
# janela.geometry("300x300")
# janela.configure(bg="black")

#     # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a quantidade de Bar: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# lbl_psi = tk.Label(janela, text="Digite o valor do PSI: ") 
# lbl_psi.grid(row=1, column=0, pady=10, padx=10)

# bar_usuario = tk.Entry(janela, font=("Arial", 12))
# bar_usuario.grid(row=0, column=1, pady=10, padx=10)

# psi_usuario = tk.Entry(janela, font=("Arial", 12))
# psi_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 4

# import tkinter as tk
# from tkinter import messagebox

# def janela_bemvindo():

#     numero1 = float(media1_usuario.get())
#     numero2 = float(media2_usuario.get())
#     numero3 = int(media3_usuario.get())
#     resultado = (numero1) + (numero2) + (numero3)
#     resultado /3

#     if  numero1 == "" and numero2 -- "" and resultado == "":
#         messagebox.showwarning("Digite as 3 notas:  ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"A sua média é: {resultado}")
   

#     # Janela
# janela = tk.Tk()
# janela.title("Calculo")
# janela.geometry("300x300")
# janela.configure(bg="black")

#     # Componentes
# lbl_nota1 = tk.Label(janela, text="Digite a primeira nota: ")
# lbl_nota1.grid(row=0, column=0, pady=10, padx=10)

# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota: ") 
# lbl_nota2.grid(row=1, column=0, pady=10, padx=10)

# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota: ") 
# lbl_nota3.grid(row=2, column=0, pady=10, padx=10)

# media1_usuario = tk.Entry(janela, font=("Arial", 12))
# media1_usuario.grid(row=0, column=1, pady=10, padx=10)

# media2_usuario = tk.Entry(janela, font=("Arial", 12))
# media2_usuario.grid(row=1, column=1, pady=10, padx=10)

# media3_usuario = tk.Entry(janela, font=("Arial", 12))
# media3_usuario.grid(row=2, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 5

import tkinter as tk
from tkinter import messagebox

def janela_bemvindo():

    numero1 = float(temeperatura_usuario.get())
   
  

    if  numero1 == "":
        messagebox.showwarning("Bem-Vindo", "Está abaixo de 40°C: BAIXA CARGA")

    elif:
    messagebox.showinfo("Bem-Vindo", "Está entre 40°C e 70°C: NORMAl")

    else:
        messagebox.showinfo("Bem-Vindo", "")
   

    # Janela
janela = tk.Tk()
janela.title("Calculo")
janela.geometry("300x300")
janela.configure(bg="black")

    # Componentes
lbl_mensagem = tk.Label(janela, text="Digite a temperatura do motor: ")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)


bar_usuario = tk.Entry(janela, font=("Arial", 12))
bar_usuario.grid(row=0, column=1, pady=10, padx=10)


btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

janela.mainloop()