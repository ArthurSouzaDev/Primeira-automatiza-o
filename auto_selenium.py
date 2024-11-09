from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
#Importações das bibliotecas necessárias

def buttonClick(identificador): #Função criada para clicar
    button = driver.find_element(By.XPATH,identificador)
    sleep(1)
    button.click()
    sleep(2)
    
def keysClick(identificador): #Função criada para digitar
    elem = driver.find_element(By.XPATH,identificador)
    sleep(1)
    elem.click()
    elem.send_keys("CGU DO ALUNO") #Seu CGU aqui
    
driver = webdriver.Firefox()
#Webdriver do firefox, lembrando que o GeckoDriver tem que ser colocado na pasta
driver.get("https://servicos.ulbra.br/ALEPH")
#Driver.get recebendo o endereço da Ulbra

usuarioAcesso = buttonClick("/html/body/table/tbody/tr[2]/td[4]/a")
cguAcesso = keysClick("/html/body/form/table/tbody/tr[1]/td[2]/input")
identifica = buttonClick("/html/body/form/table/tbody/tr[2]/td/input")
emprestimoAcesso = buttonClick("/html/body/table[3]/tbody/tr[1]/td[1]/a")
renovarEmprestimo = buttonClick('//*[@id="bold"]')
#Variáveis de acesso 

driver.quit()  # Use quit() para fechar o navegador completamente
print("Sucesso! Os livros foram renovados!")
