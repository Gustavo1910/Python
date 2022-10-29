import random
from rich import print
import os
import time

# Parte inicial do codigo
def visual_codigo():
    os.system('cls')
    print('')
    print('[on green]-=-[/]' * 13)
    print('[on green]|[/]                                     [on green]|[/]')
    print(
        '[on green]|[/]     [bold]      [italic][underline][white]Bem vindo(a)![/][/][/][/]             [on green]|\n|[/]                                     [on green]|[/]')
    print('[on green]|[/] vou pensar um numero entre [bold]1[/] a [bold]100[/]. [on green]|[/]')
    print('[on green]|[/]     Tente descobir esse numero.     [on green]|[/]')
    print('[on green]|[/]                                     [on green]|[/]')
    print('[on green]-=-[/]' * 13)
    print('')
    time.sleep(3)
    os.system('cls')


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
                time.sleep(6)
                os.system('cls')
            elif chute > numero:
                print(f'[bold][white]O numero [/][/][bold]{chute}[/][bold][white] é maior que meu número, tente um número menor[/][/]')
                tentativa +=1
                time.sleep(1)
            elif chute < numero:
                print(f'[bold][white]O numero [/][/][bold]{chute}[/][bold][white] é menor que meu número, tente um número maior[/][/]')
                tentativa += 1
                time.sleep(1)
            elif chute == numero:
                print(f'\nUaauuu você acertou, meu numero era [green1][bold]{numero}[/][/]!!')
                print(f'Você tentou [green1][bold]{tentativa}x[/][/]')
                opcao=input("Vamos jogar de novo?  (s/n)  ").strip()[0]
                if opcao.lower() == "s":
                    os.system('cls')
                    print('\n[green][bold]Reiniciando...[/][/]')
                    time.sleep(1)
                    os.system('cls')
                    continue
                elif opcao.lower() == "n":
                    os.system('cls')
                    print('\n[bold][white]Muito obrigado por jogar :heart:[/][/]      ')
                    time.sleep(1)
                    os.system('cls')
                    break
        except ValueError:
            print('[red][bold]Digite um numero inteiro[/][/]')
            time.sleep(1)
            os.system('cls')





print('')
input('Digite ENTER para iniciar ')
visual_codigo()
tentativa = 0
numero = gerador_numero()
Base_codigo(numero, tentativa)









