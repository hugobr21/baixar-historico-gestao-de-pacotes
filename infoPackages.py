from minhas_funcoes.setup_programa import setupPrograma
from minhas_funcoes.classes_inventario import pacotes
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import pyperclip
import re

# setup_programa = setupPrograma(perfilFirefox1=r'C:\Users\vdiassob\AppData\Roaming\Mozilla\Firefox\Profiles\4p8iewsw.gestaodepacotes1',
# perfilFirefox2=r'C:\Users\vdiassob\AppData\Roaming\Mozilla\Firefox\Profiles\elaguh96.gestaodepacotes2',
# caminhoFirefox=r'C:\Program Files\Mozilla Firefox\firefox.exe')

setup_programa = setupPrograma()
setup_programa.carregar_parametros()

instancia_pacotes = pacotes()
instancia_pacotes.ids += [re.search('\d\d\d\d\d\d\d\d\d\d\d', i)[0] for i in pyperclip.paste().split('\n') if str(type(re.search('\d\d\d\d\d\d\d\d\d\d\d', i)))!="<class 'NoneType'>"]

options1 = Options()
options1.add_argument("-profile")
options1.add_argument(setup_programa.perfilFirefox1)
options1.binary_location = setup_programa.caminhoFirefox
driver1 = webdriver.Firefox(options=options1)
driver1.get('https://envios.mercadolivre.com.br/logistics/management-packages')
input('\nPara iniciar o processo pressione ENTER.\n')
driver1.set_page_load_timeout(15)

while True:
    try:
        instancia_pacotes.consolidar_historico_sem_usuario(driver1,By,pd)
        driver1.quit()
        print('\nProcesso completo com sucesso!\n')
        break
    except:
        driver1.quit()
        driver1 = webdriver.Firefox(options=options1)
        driver1.get('https://envios.mercadolivre.com.br/logistics/management-packages')
        driver1.set_page_load_timeout(15)
        pass