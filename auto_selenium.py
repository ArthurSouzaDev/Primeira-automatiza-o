#Importando inicialmente selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Nas linhas abaixo foi importado webdriveManager que atualiza o webdriver automaticamente
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager

#Na linha abaixo foi adicionado Options para deixar o navegador no modo Headless, apenas interface gráfica 
#para reduzir custos de processamento
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

#Excepted conditions abaixo
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

def main():
    navegador = input("Escolha o navegador (chrome, firefox, edge): ").strip().lower()
    
    try:
        # Inicializa o driver com o navegador escolhido
        driver = inicializar(navegador)
        
        # Acessa o site
        driver.get("https://servicos.ulbra.br/ALEPH")
        codigo = input("Digite o seu CGU: ")        

        # Fluxo de automação
        buttonClick("/html/body/table/tbody/tr[2]/td[4]/a")  # Acessar usuário/renovação
        keysClick("/html/body/form/table/tbody/tr[1]/td[2]/input", codigo)  # Enviar CGU
        buttonClick("/html/body/form/table/tbody/tr[2]/td/input")  # Confirmar login
        buttonClick("/html/body/table[3]/tbody/tr[1]/td[1]/a")  # Acessar empréstimos
        buttonClick('//*[@id="bold"]')  # Renovar livros
        
        identificador = "/html/body/div[2]/p[2]"  #XPath da mensagem esperada! 
        mensagem_esperada = "Não há empréstimos em seu nome no momento."

        # Verificar a mensagem
        if verificar_mensagem(identificador, mensagem_esperada) == True:
            print("Sucesso! Os livros foram renovados!")
        else:
            print("Mensagem de erro ou situação esperada não encontrada.")

    except Exception as e:
        print(f"Erro no fluxo principal: {e}")
    
    finally:
        print("Programa encerrado com sucesso!")

        driver.delete_all_cookies()
        driver.quit()

# Verifica se o script é executado diretamente
if __name__ == "__main__":
    main()