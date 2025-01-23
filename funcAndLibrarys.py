from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Importações das bibliotecas necessárias

def inicializar(navegador="chrome"):
    global driver #Transformadno em variável global para ser acessada nas funções sem ter que ser chamada como parâmetro
    navegador = navegador.lower()
    if navegador == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless") #Modo headless para reduzir uso de recursos
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif navegador == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")  # Modo headless para o Firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    elif navegador == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")  # Modo headless para o Edge
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)    
    else:
        raise ValueError(f"Navegador não suportado: {navegador}")

    return driver

#Verificando mensagem para ter certeza se o livro foi renovado ou não!
def verificar_mensagem(identificador, mensagem_esperada):
    try:
        # Espera até que o elemento com a mensagem esteja visível (máximo 10 segundos)
        elemento = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, identificador))
        )
        texto = elemento.text
        if texto != mensagem_esperada:
            print(f"Livros foram renovados: {texto}")
            return True
        else:
            print("Não há empréstimo ativos!.")
            return False
    except Exception as e:
        print(f"Erro ao verificar a mensagem: {e}")
        return False

#Utilizando o expected conditions nas duas funções para ser mais útil que o sleep, assim 
def buttonClick(identificador):  # Função criada para clicar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador))#variável identificador recebe o xpath onde deve ser clicado!
        )
        button.click()
    except Exception as e:
        print(f"Ocorreu um erro ao clicar no botão: {e}")  # Garantindo a exibição do erro

def keysClick(identificador,codigo): #Função criada para digitar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador)) #variável identificador recebe o xpath onde deve ser clicado!
        ).send_keys(codigo)
    except Exception as e:
        print(f"Erro ao digitar no campo: {e}")
