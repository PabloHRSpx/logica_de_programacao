# projeto cancela automatica

print("Escolha uma opção de entrada:")
print("1 - Pegar Ticket")
print("2 - Usar TAG")
print("3 - Ligar para o interfone")

escolhido = input("Qual opção você deseja escolher?")

if escolhido == "1":
    print("Ticket Liberado!")
    placa = input("Escreva a placa do seu veículo:")
    hora1 = float(input("Digite a hora:"))
    print(f"Placa do veículo:", placa, "\nhora de entrada:", hora1)
    valor_cobrado1 = float(input("Digite o valor cobrado:"))
    saida1 = float(input("Digite a hora da saída:"))
    tempo_total1 = saida1 - hora1
    print(f"O tempo do estacionamento é:", tempo_total1, "horas")
    valor_estacionamento = tempo_total1 * valor_cobrado1
    print(f"O valor a ser cobrado foi de R${valor_estacionamento:.2f}")

elif escolhido == "2":
    print("TAG Liberada!")
    print("Será cobrado na sua fatura!")
elif escolhido == "3":
    print("Liberando acesso pelo interfone")
    print("Sua saída deverá ser feita também pelo interfone")
else:
    print("Obrigado pela visita!")
