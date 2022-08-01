import time
from rich import print
import os

while True:
    conta = input("Que tipo de conta deseja fazer? (*, /, +, -) ")

    if conta == "*" or conta == "/" or conta == "+" or conta =="-":
        os.system('cls')
        print('')
        print('[on red][white][bold]aguarde.........[/][/][/]')
        time.sleep(1)
        os.system('cls')

        if conta == '*':
            valor1 = input("Entre com o primeiro valor: ")
            valor2 = input("Entre com o segundo valor: ")
            os.system('cls')

            if not valor1.isdigit() or not valor2.isdigit():
                os.system('cls')
                print('')
                print('[red][bold]O valor insirido não é valido:x: ')
                time.sleep(0.9)
                os.system('cls')
                print('')
                print('[red][bold]Porfavor insira apenas numeoros reais!!![/][/]')
                os.system('cls')
                pass




            else:
                valor1= int(valor1)
                valor2= int(valor2)
                valor3= valor2*valor1
                print('')
                print('[on red][white][bold]aguarde.........[/][/][/]')
                time.sleep(0.5)
                os.system('cls')
                print('')
                print('[green][bold]E a resposta é...[/][/]')
                time.sleep(1.2)
                os.system('cls')
                print('')
                print(f'[bold]{valor3}[/]')
                time.sleep(5)
                os.system('cls')
                continuar = input("Deseja fazer outra conta? (s/n)  ")
                continuar = continuar.upper()
                os.system('cls')
                print('')
                print('[green][bold]Carregando...[/][/]')
                time.sleep(1)
                os.system('cls')
                if continuar =='S':
                    pass

                elif continuar=='N':
                    break

        elif conta == '/':
            valor1 = input("Entre com o primeiro valor: ")
            valor2 = input("Entre com o segundo valor: ")
            os.system('cls')

            if not valor1.isdigit() or not valor2.isdigit():
                os.system('cls')
                print('')
                print('[red][bold]O valor insirido não é valido:x: ')
                time.sleep(0.9)
                os.system('cls')
                print('')
                print('[red][bold]Porfavor insira apenas numeoros reais!!![/][/]')
                os.system('cls')
                pass




            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                valor3 = valor1 / valor2
                print('')
                print('[on red][white][bold]aguarde.........[/][/][/]')
                time.sleep(0.5)
                os.system('cls')
                print('')
                print('[green][bold]E a resposta é...[/][/]')
                time.sleep(1.2)
                os.system('cls')
                print('')
                print(f'[bold]{valor3}[/]')
                time.sleep(5)
                os.system('cls')
                continuar = input("Deseja fazer outra conta? (s/n)  ".upper())
                continuar = continuar.upper()
                os.system('cls')
                print('')
                print('[green][bold]Carregando...[/][/]')
                time.sleep(1)
                os.system('cls')
                if continuar == 'S':

                    pass

                elif continuar == 'N':
                    break


        elif conta == '+':
            valor1 = input("Entre com o primeiro valor: ")
            valor2 = input("Entre com o segundo valor: ")
            os.system('cls')

            if not valor1.isdigit() or not valor2.isdigit():
                os.system('cls')
                print('')
                print('[red][bold]O valor insirido não é valido:x: ')
                time.sleep(0.9)
                os.system('cls')
                print('')
                print('[red][bold]Porfavor insira apenas numeoros reais!!![/][/]')
                os.system('cls')
                pass




            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                valor3 = valor2 + valor1
                print('')
                print('[on red][white][bold]aguarde.........[/][/][/]')
                time.sleep(0.5)
                os.system('cls')
                print('')
                print('[green][bold]E a resposta é...[/][/]')
                time.sleep(1.2)
                os.system('cls')
                print('')
                print(f'[bold]{valor3}[/]')
                time.sleep(5)
                os.system('cls')
                continuar = input("Deseja fazer outra conta? (s/n)  ".upper())
                continuar = continuar.upper()
                os.system('cls')
                print('')
                print('[green][bold]Carregando...[/][/]')
                time.sleep(1)
                os.system('cls')
                if continuar == 'S':

                    pass

                elif continuar == 'N':
                    break


        elif conta == '-':
            valor1 = input("Entre com o primeiro valor: ")
            valor2 = input("Entre com o segundo valor: ")
            os.system('cls')

            if not valor1.isdigit() or not valor2.isdigit():
                os.system('cls')
                print('')
                print('[red][bold]O valor insirido não é valido:x: ')
                time.sleep(0.9)
                os.system('cls')
                print('')
                print('[red][bold]Porfavor insira apenas numeoros reais!!![/][/]')
                os.system('cls')
                pass




            else:
                valor1 = int(valor1)
                valor2 = int(valor2)
                valor3 = valor1 - valor2
                print('')
                print('[on red][white][bold]aguarde.........[/][/][/]')
                time.sleep(0.5)
                os.system('cls')
                print('')
                print('[green][bold]E a resposta é...[/][/]')
                time.sleep(1.2)
                os.system('cls')
                print('')
                print(f'[bold]{valor3}[/]')
                time.sleep(5)
                os.system('cls')
                continuar = input("Deseja fazer outra conta? (s/n)  ".upper())
                continuar = continuar.upper()
                os.system('cls')
                print('')
                print('[green][bold]Carregando...[/][/]')
                time.sleep(1)
                os.system('cls')
                if continuar == 'S':

                    pass

                elif continuar == 'N':
                    break





    else:
        os.system('cls')
        print('')
        print('[on red][white][bold]aguarde.........[/][/][/]')
        time.sleep(1)
        os.system('cls')
        print()
        print('[red][bold]> O caracter inserido não possivel reconhecer...[/][/]')
        time.sleep(3)
        os.system('cls')
        pass



