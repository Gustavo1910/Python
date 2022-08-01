import random
import os
import time
from rich import print

letras_minusculas = "abcdfghijklmnopqrstuvwxyz"
letras_maiusculas = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"
user = letras_maiusculas + letras_minusculas + numeros + simbolos
quantidade_caracteres = 8

senha = ''.join(random.sample(user, quantidade_caracteres))

print('')
print('[reen]Gerando senha....')
time.sleep(2.3)
os.system('cls')
print('')
print(f"{senha}")