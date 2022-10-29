import os
import re
import shutil
import time
import moviepy.editor as mp
from playsound import playsound
from pytube import YouTube
from rich import print
print()
print('[bold][white]  Clique ENTER para iniciar[/][/]')
input('')
os.system('cls')
while True:
    link = input('Entre com o link do Youtube da musica: ')
    yt = YouTube(link)

    # Cria uma pasta para guarda a musica
    def pasta():
        pasta_teste = 'a/'
        if (not os.path.exists(pasta_teste)):
            os.mkdir('C:/' + pasta_teste)

    # Baixa a musica em mp4 e converte para mp3
    def song():
        path = 'C:/a/'
        ys = yt.streams.filter(only_audio=True).first().download(path)


        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)

                os.system('cls')

    # Dá play na musica
    def play_playsound():

        time.sleep(5)
        print(playsound('C:/a/a.mp3'))

    # Muda o nome da musica
    def name_song():
        path = 'C:/a/'
        for file_name in os.listdir(path):
            old_name = path + file_name
            new_name = path + 'a' + '.mp3'
            os.rename(old_name,new_name)
    # Remove a pasta e a musica
    def remove_song():
        time.sleep(2)
        shutil.rmtree('C:/a/')

    def clean():
        os.system('cls')

    pasta()
    time.sleep(1)
    song()
    name_song()
    time.sleep(4)
    play_playsound()
    remove_song()
    clean()
    opcao=input("Vamos escutar mais?  (s/n)  ").strip()[0]
    if opcao.lower() == "s":
        os.system('cls')
        print('\n[green][bold]Reiniciando...[/][/]')
        time.sleep(1)
        os.system('cls')
        continue
    elif opcao.lower() == "n":
        os.system('cls')
        print('\n[bold][white]Até a proxima :heart:[/][/]      ')
        time.sleep(1)
        os.system('cls')
        break

