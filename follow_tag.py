from instapy import InstaPy
import PySimpleGUI as sg



class TelaPython:
    def __init__(self):
        #Layout:
        sg.theme('DarkBlue')
        self.layout = [
            [sg.Text('Login:',size=(10,0)), sg.InputText(size=(20,0))],
            [sg.Text('Senha:',size=(10,0)), sg.InputText(size=(20,0))],
            [sg.Text('Tag:',size=(10,0)), sg.InputText(size=(20,0))],
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
login, password, tag = tela.run() # Aqui tu faz o unpack da tua tupla em variáveis.




# COMMANDS FOR BOT:

# Commands Login:
session = InstaPy(username=login, password=password, headless_browser=True)
session.login()


# COMMANDS GENERAL: 
session.like_by_tags([tag], amount=5)
session.set_dont_like(["naked", "nsfw", "rape", "violence", "suicide"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)





















session = InstaPy(username="zshoes.store", password="36980293", headless_browser=True)
session.login()

# Curtir publicações seguindo a referência de tags;
session.like_by_tags(["Calçado", "tênis", "t-shirts", "shoes", "tênis nike"], amount=5)
session.set_dont_like(["naked", "nsfw", "rape", "violence", "suicide"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.end()