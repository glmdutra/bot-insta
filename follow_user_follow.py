"""RELEASE

https://pypi.org/project/instapy/0.1.0/
https://pysimplegui.readthedocs.io/en/latest/
https://pypi.org/project/selenium/
https://github.com/mozilla/geckodriver/releases

INSTALL INSTAPY: pip install instapy
INSTAL PYSIMPLEGUI: pip install pysimplegui

"""



from instapy import InstaPy
import PySimpleGUI as sg



# COMMANDS FOR BOT:

class TelaPython:
    def __init__(self):
        #Layout:
        sg.theme('DarkBlue')
        self.layout = [
           [sg.Text('Login:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Senha:',size=(10,0)), sg.InputText(password_char='*',size=(20,0))],
           [sg.Text('Seguidores:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Quantidade:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Checkbox('Modo Invisivel', default=True, size=(10,0))],
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
                return (values[0], values[1], values[2], values[3], values[4]) # retorna os tres valores como uma tupla

tela = TelaPython()
login, password, seguidores, quant, modo = tela.run() # aqui tu faz o unpack da tua tupla em variaveis




# COMMANDS FOR BOT:


# Commands Login:
session = InstaPy(username= login, password= password, headless_browser=modo)
session.login()


#Commands general:
session.set_relationship_bounds(enabled=True,
				 potency_ratio=1.34,
				  delimit_by_numbers=True,
				   max_followers=10000,
				    max_following=10000,
				     min_followers=100,
				      min_following=56)

session.follow_user_following(seguidores, amount=int(quant), randomize=False)
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
 


