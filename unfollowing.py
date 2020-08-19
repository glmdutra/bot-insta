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



class TelaPython:
    def __init__(self):
        #Layout:
        sg.theme('DarkBlue')
        self.layout = [
           [sg.Text('Login:',size=(10,0)),sg.InputText(size=(20,0))],
           [sg.Text('Senha:',size=(10,0)), sg.InputText(password_char='*',size=(20,0))],
           [sg.Text('Seguidores:',size=(10,0)),sg.InputText(size=(20,0))],
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
                return(values[0], values[1], values[2]) # Retorna os três valores como uma tupla.

tela = TelaPython()
login, password, modo = tela.run() # Aqui tu faz o unpack da tua tupla em variáveis.




# COMMANDS FOR BOT:

# Commands Login:
session = InstaPy(username=login, password=password, headless_browser=modo)
session.login()


# COMMANDS GENERAL: 

session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=601)
