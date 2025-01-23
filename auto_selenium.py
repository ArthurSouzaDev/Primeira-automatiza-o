from funcAndLibrarys import *
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