from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
#Nas linhas abaixo foi importado webdriveManager que atualiza o webdriver automaticamente
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Na linha abaixo foi adicionado Options para deixar o navegador no modo Headless, apenas interface gráfica 
#para reduzir custos de processamento
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Importações das bibliotecas necessárias

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)
#A linha de código acima atualiza automaticamente o webdriver dos navegadores sem ter que atualizar manualmente

chrome_options = Options()
chrome_options.add_argument("--headless")
#Utilizando o modo headless do navegador para otimizar e reduzir o custo de processamento.

#Utilizando o expected conditions nas duas funções para ser mais útil que o sleep, assim 
#a função só irá rodar se o elemento aparecer na tela, ao invés de apenas aguardar um tempo específico
def buttonClick(identificador): #Função criada para clicar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador))
        )
        button.click()
    except Exception as e:
        print(f"Ocorreu um erro 1: {e}")


def keysClick(identificador): #Função criada para digitar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador))
        )
        button.click()
        button.send_keys("135688210")  # Seu CGU aqui
    except Exception as e:
        print(f"Ocorreu um erro 2: {e}")
    
driver.get("https://servicos.ulbra.br/ALEPH")
#Driver.get recebendo o endereço da Ulbra

#Após importar as bibliotecas e criar a função, iremos rodar o código nas variáveis abaixo com a xpath de cada elemento
usuarioAcesso = buttonClick("/html/body/table/tbody/tr[2]/td[4]/a")
cguAcesso = keysClick("/html/body/form/table/tbody/tr[1]/td[2]/input")
identifica = buttonClick("/html/body/form/table/tbody/tr[2]/td/input")
emprestimoAcesso = buttonClick("/html/body/table[3]/tbody/tr[1]/td[1]/a")
renovarEmprestimo = buttonClick('//*[@id="bold"]')
#Variáveis de acesso 

driver.quit()  # Use quit() para fechar o navegador completamente
print("Sucesso! Os livros foram renovados!")
