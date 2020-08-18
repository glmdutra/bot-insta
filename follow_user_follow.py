"""RELEASE

https://pypi.org/project/instapy/0.1.0/
https://pysimplegui.readthedocs.io/en/latest/
https://pypi.org/project/selenium/


INSTALL INSTAPY: pip install instapy
INSTAL PYSIMPLEGUI: pip install pysimplegui

"""



from instapy import InstaPy
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout:
        sg.theme('DarkAmber')
        self.layout = [
           [sg.Text('Login:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Senha:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Seguidores:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Button('Iniciar'), sg.Button('Cancelar')]
        ]

    def run(self):
        #Janela:
        window = sg.Window("Dados do Usuário", self.layout)

        # aqui tu pode colocar um eventloop
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                exit() # aqui o user clicou em Cancelar e o programa termina
            elif event == 'Iniciar':
                window.close()
                return (values[0], values[1], values[2]) # retorna os tres valores como uma tupla

tela = TelaPython()
login, password, seguidores = tela.run() # aqui tu faz o unpack da tua tupla em variaveis




# COMMANDS FOR BOT:


# Commands Login:
session = InstaPy(username= login, password= password, headless_browser=True)
session.login()

#Commands general:
session.follow_user_following(seguidores, amount=100, randomize=False, sleep_delay=60)
"""session.like_by_tags(["Calçado", "tênis", "t-shirts", "shoes", "tênis nike"], amount=5)"""
session.set_dont_like(["naked", "nsfw", "rape", "violence", "suicide"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
 


