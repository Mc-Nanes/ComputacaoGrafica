# Conversor de Cores RGB para HSI

Uma aplicação em Python que converte valores de cores do modelo RGB para o modelo HSI usando uma interface gráfica em Tkinter. O usuário insere valores RGB e visualiza uma representação da cor correspondente. A aplicação então converte essa cor para o modelo HSI, exibe os valores e mostra uma representação visual da cor no espaço HSI.

## Funcionalidades

- **Entrada de cores RGB**: Insira valores entre 0 e 255 para os canais vermelho (R), verde (G) e azul (B).
- **Exibição visual**: Um retângulo exibe a cor RGB com base nos valores inseridos.
- **Conversão para HSI**: Converte os valores RGB para HSI e exibe os valores de Matiz, Saturação e Intensidade.
- **Limpeza**: O botão "Limpar" redefine os valores e retorna os retângulos ao estado inicial, sem preenchimento.
- **Validação de entrada**: Verifica se os valores de entrada estão no intervalo 0-255 e exibe uma mensagem de erro, se necessário.

## Tecnologias Utilizadas

<img src="https://static.wikia.nocookie.net/lpunb/images/b/b1/Logo_Python.png/revision/latest?cb=20130301171443" alt="Logo do Python" width="100" height="100" />

## Como Funciona

1. O usuário insere valores de **R**, **G** e **B** (entre 0 e 255). Cada campo exibe o número digitado em uma cor correspondente ao canal (vermelho para R, verde para G e azul para B).
2. Clicar no botão **Converter** faz a aplicação:
   - Validar os valores de entrada.
   - Exibir a cor RGB correspondente no retângulo.
   - Converter RGB para HSI e mostrar os valores de Matiz, Saturação e Intensidade.
3. Clicar no botão **Limpar** redefine os valores e os retângulos para o estado inicial.
