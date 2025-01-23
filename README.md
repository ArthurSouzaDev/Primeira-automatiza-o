# Automação de Renovação de Livros - Selenium

Este projeto implementa uma automação utilizando Selenium para renovar livros no sistema da **ULBRA**. A aplicação simula interações no navegador e permite que o usuário escolha entre os navegadores Chrome, Firefox ou Edge para executar o script.

## 🚀 Funcionalidades

- Suporte aos navegadores Chrome, Firefox e Edge.
- Execução no modo **headless** (sem interface gráfica) para melhor desempenho.
- Login automatizado no sistema da ULBRA.
- Renovação de livros emprestados.
- Verificação de mensagens de confirmação ou erro.

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [WebDriverManager](https://github.com/SergeyPirogov/webdriver_manager)

## 📋 Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.8+](https://www.python.org/downloads/)
- Gerenciador de pacotes `pip`

## ⚙️ Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
Instale as dependências:

bash
Copiar
Editar
````bash
pip install -r requirements.txt
````
Adicione o arquivo requirements.txt com as seguintes dependências:

```bash
selenium
webdriver_manager
```
🚦 Como Usar
Execute o script:

```bash
python nome-do-script.py
``` 
Escolha o navegador (Chrome, Firefox ou Edge).

Insira o seu CGU quando solicitado.

A automação realizará o login, acessará a área de empréstimos e tentará renovar os livros disponíveis.

📝 Estrutura do Código

Funções principais:

inicializar(navegador): Configura o WebDriver com o navegador selecionado.
buttonClick(identificador): Clica em elementos na página.
keysClick(identificador, codigo): Preenche campos de texto.
verificar_mensagem(identificador, mensagem_esperada): Verifica mensagens exibidas na página.
Fluxo principal (main):
Inicializa o navegador escolhido.
Realiza as etapas de login, navegação e renovação.
Exibe mensagens de sucesso ou erro.

🔍 Observações

O script está configurado para acessar diretamente o site da ULBRA no endereço: https://servicos.ulbra.br/ALEPH.
Certifique-se de que o XPath utilizado no código corresponde ao layout atual do site, pois mudanças no design podem causar falhas na automação.

🛡️ Cuidados
Este projeto é apenas para fins educacionais. Certifique-se de ter permissão para automatizar ações no site antes de usar.
Use o script de forma responsável, respeitando os termos de uso do serviço.

📧 Contato
Para dúvidas ou sugestões, sinta-se à vontade para entrar em contato comigo: seu-email@exemplo.com

Feito com ❤️ e Selenium.

Caso precise de mais personalizações ou ajustes, é só avisar! 😊
