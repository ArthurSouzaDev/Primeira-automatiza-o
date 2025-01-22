from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#Nas linhas abaixo foi importado webdriveManager que atualiza o webdriver automaticamente
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.chrome import ChromeDriverManager

#Na linha abaixo foi adicionado Options para deixar o navegador no modo Headless, apenas interface gráfica 
#para reduzir custos de processamento
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Importações das bibliotecas necessárias

def inicializar(navegador="chrome"):
    navegador = navegador.lower()
    if navegador == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless") #Modo headless para reduzir uso de recursos
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif navegador == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif navegador == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Navegador não suportado: {navegador}")

    return driver

#Utilizando o expected conditions nas duas funções para ser mais útil que o sleep, assim 
def buttonClick(driver, identificador):  # Função criada para clicar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador))
        )
        button.click()
    except Exception as e:
        print(f"Ocorreu um erro ao clicar no botão: {e}")  # Garantindo a exibição do erro

def keysClick(driver,identificador,codigo): #Função criada para digitar
    try:
        # Espera até que o botão esteja clicável (máximo 10 segundos)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, identificador))
        )
        button.click()
        button.send_keys(codigo)  # Seu CGU aqui
    except Exception as e:
        print(f"Erro ao digitar no campo: {e}")
    
def main():
    navegador = input("Escolha o navegador (chrome, firefox, edge): ").strip().lower()
    
    try:
        # Inicializa o driver com o navegador escolhido
        driver = inicializar(navegador)
        
        # Acessa o site
        driver.get("https://servicos.ulbra.br/ALEPH")
        
        codigo = input("Digite o seu CGU: ")

        # Fluxo de automação
        buttonClick("/html/body/table/tbody/tr[2]/td[4]/a")  # Acessar página
        keysClick("/html/body/form/table/tbody/tr[1]/td[2]/input", codigo)  # Enviar CGU
        buttonClick("/html/body/form/table/tbody/tr[2]/td/input")  # Confirmar login
        buttonClick("/html/body/table[3]/tbody/tr[1]/td[1]/a")  # Acessar empréstimos
        buttonClick('//*[@id="bold"]')  # Renovar livros
        print("Sucesso! Os livros foram renovados!")

    except Exception as e:
        print(f"Erro no fluxo principal: {e}")
    
    finally:
        print("Programa encerrado com sucesso!")
        driver.quit()

# Verifica se o script é executado diretamente
if __name__ == "__main__":
    main()