import random
from rich import print
import os
import time

# Gerar numero
def gerador_numero():
    numero_gerado = random.randrange(1, 100)
    return numero_gerado


# criar base para o programa

def Base_codigo(numero, tentativa):
    while True:
        try:
            chute = int(input('\nDigite um numero:'))
            if chute > 100 or chute < 1:
                os.system('cls')
                print('\n[red][bold]Porfavor insira um valor entre 1 a 100, tente novamento...[/][/]')
                time.sleep(3)
                os.system('cls')
            elif chute > numero:
                print(f'\nO numero [bold]{chute}[/] é maior que meu número, tente um número menor')
                tentativa +=1
                time.sleep(1)
            elif chute < numero:
                print(f'\n O numero [bold]{chute}[/] é menor que meu número, tente um número maior')
                tentativa += 1
                time.sleep(1)
            elif chute == numero:
                print(f'\nUaauuu você acertou, meu numero era [green1][bold]{numero}[/][/]!!')
                print(f'Você tentou [green1][bold]{tentativa}x[/][/]')
                opcao=input("Vamos jogar de novo?  (s/n)  ")
                if opcao.lower() == "s":
                    os.system('cls')
                    print('\n[green][bold]Reiniciando...[/][/]')
                    time.sleep(1)
                    os.system('cls')
                    continue
                elif opcao.lower() == "n":
                    os.system('cls')
                    print('\nMuito obrigado por jogar :heart:  ')
                    time.sleep(1)
                    os.system('cls')
                    break
        except ValueError:
            print('[red][bold]Digite um numero inteiro[/][/]')
            time.sleep(1)
            os.system('cls')







input('Digite ENTER para iniciar ')
tentativa = 0
numero = gerador_numero()
Base_codigo(numero, tentativa)









