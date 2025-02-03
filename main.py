import random

def Numero_secreto():
    Numero= random.randint(1,100)
    Tentativas = 0
    
    print('Tente adivinhar o número entre 1 e 100:')
    
    while True:
        try:
            Palpite = int(input("Digite seu palpite: "))
            Tentativas += 1
            
            if Palpite < 1 or Palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            
            if Palpite < 1 or Palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            
            if Palpite > Numero:
                print("O número secreto é menor!")
            elif Palpite < Numero:
                print("O número secreto é maior!")
            else:
                print(f"Parabéns! Você acertou o número {Numero} em {Tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido!")
            
Numero_secreto()