print("Elevador no andar: 0(térreo)")
andar_inicial = int(input("Qual andar você quer chamar o elevador?"))

while True:
    try:
        pessoas = int(input("Quantas pessoas vai no elevador: "))
        
        if pessoas <= 5:
            print("Quantidade de pessoas no limite")
        else:
            print("Passou do limite de pessoas!")
            break
    
        print(f"O andar atual: {andar_inicial} , quantidade de pessoas no elevador: {pessoas}")
    
        andar = int(input("Digite o andar de o a 10"))
    
        if andar < 0  or andar > 10:
            raise ValueError("Andar inválido. Por favor, coloque um número entre 0 a 10")
    
        print(f"Elevador está no andar {andar_inicial}, agora está indo para o andar {andar}")
        andar_inicial = andar
        print(f"Chegamos ao andar {andar_inicial}")

        if input("Quer escolher outro andar?").lower() != 'sim':
            print("Obrigado por usar o elevador!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[x]' if listagem == andar_inicial else '[ ]'}")
    
    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente")
        break












