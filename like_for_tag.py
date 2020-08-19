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


#COMMANDS FOR BOT:

class TelaPython:
    def __init__(self):
        #Layout:
        sg.theme('DarkBlue')
        self.layout = [
           [sg.Text('Login:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Senha:',size=(10,0)), sg.InputText(password_char='*',size=(20,0))],
           [sg.Text('Seguir Tag:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Quantidade:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Checkbox('Modo Invisivel', default=True, size=(10,0))],
           [sg.Button('Iniciar'), sg.Button('Cancelar')]
        ]

    def run(self):

        #Janela
        window = sg.Window("Dados do Usuário", self.layout)

        # Aqui eu coloco um EventLoop para o Iniciar e Cancelar
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                exit() # Aqui o user clicou em cancelar e o programa termina

            elif event == 'Iniciar':
                window.close()
                return(values[0], values[1], values[2], values[3], values[4]) # Retorna os três valores como uma tupla.

tela = TelaPython()
login, password, tag, quant, modo = tela.run() # Aqui tu faz o unpack da tua tupla em variáveis.




# COMMANDS FOR BOT:

# Commands Login:
session = InstaPy(username=login, password=password, headless_browser=modo)
session.login()


# COMMANDS GENERAL: 
session.set_relationship_bounds(enabled=True,
				 potency_ratio=1.34,
				  delimit_by_numbers=True,
				   max_followers=8500,
				    max_following=4490,
				     min_followers=100,
				      min_following=56)

session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
session.like_by_tags([tag], amount=int(quant), interact=True)
session.follow_by_tags([tag], amount=int(quant), interact=True)
session.set_dont_like(["naked", "nsfw", "rape", "violence", "suicide"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)




















