from sys import exit
from os import popen
from time import sleep
from pyautogui import alert
from pyautogui import prompt
from tkinter import messagebox as mb

# Abre o cmd e inicializa o repo # ---------------------->
git_init = popen("git init")

# Adiciona os arquivos na lista para commit # ---------------------->
git_add = popen("git add -A")

# Altera para a branch main # ---------------------->
popen("git branch -M main")
popen("git branch")

# Aguarda input do usuario # ---------------------->
commit = prompt("Mensagem para o commit")

comm = mb.askyesno('Commit', 'Sim para Commit')
if not comm:
    exit()

# Realiza o commit # ---------------------->
popen(f'git commit -m "{commit}"') 

# Pergunta ao usuario se ele quer subir o push # ---------------------->
'''push = mb.askyesno('Push', 'Deseja fazer o Push ?')
if not push:
    exit()'''

# Realiza o push para o repo no Github # ---------------------->
popen("git push -f origin main")

alert("Feito!")

# abre o repositorio no navegador
popen("start brave https://github.com/oliveirascof/team-stats")

# encerra o script
exit()