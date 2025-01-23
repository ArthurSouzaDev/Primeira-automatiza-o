Além das instruções aqui estará a documentação do projeto de automatização, e a razão para essa automatização ser criada! 
Razão da criação:Esqueci de renovar e acabei pagando uma taxa alta de livros na biblioteca, então criei essa automatização para não ter que preocupar

Bibliotecas e motivo de serem importadas para nosso código!
Linha 1 a 4 são importação do selenium e webdrivers by

linha 7 a 12 são linhas do webdriver Manager de cada navegador, escolhi ter alguns navegadores diferentes, pelo menos 1 dos 3 escolhidos o usuário irá ter instalado na máquina, eles são Chrome, firefox e Edge! 

Linha 16 a 18 São linhas importanto as opções de cada navegador exclusivamente para ativar o modo headless de cada um, uma explicação rápida sobre o modo headless: Ele serve para evitar custos de processamento, ele não irá mostrar para o usuário, ele irá rodar "Por fora dos panos"

Linha 21 a 23 é referente ao expected conditions, que foi usado no lugar do Sleep, deixando o código mais "Elegante" e prático

Após importação das bibliotecas iremos seguir com as funções!

Função inicializar  