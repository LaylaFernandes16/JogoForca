# PROJETO FORCA
Olá, esse projeto é um Jogo da Forca em python, criado como um exercício para melhorar minhas habilidades de programação de uma forma prática e divertida.

--> O programa escolhe uma palavra aleatória de uma lista pré-definida e o jogador deve adivinhar a palavra letra por letra. O jogo termina quando o jogador acerta todas as letras ou perde após 6 tentativas incorretas.

## COMO FUNCIONA:
1. O programa escolhe uma palavra aleatória da lista palavras.

2. O jogador recebe a dica visual com traços (_) representando cada letra da palavra.

3. O jogador digita uma letra por vez:
 - Se a letra estiver correta, ela aparece no lugar certo.
 - Se a letra estiver errada, é contabilizada uma tentativa.

4. O jogo termina quando: 
 - O jogador acerta todas as letras (vitória).
 - O jogador comete 6 erros (derrota).

## ESTRUTURA DO CÓDIGO:
 - palavras: lista com palavras possíveis para o jogo.

 - choice(palavras): escolhe a palavra aleatoriamente.

 - tentativa: contador de erros, máximo 6.

 - letra_certa e letra_errada: listas para armazenar letras já tentadas.

 - tracos: lista que mostra as letras acertadas ou _ para as ainda não descobertas.

## POSSÍVEIS MELHORIAS:
 - Adicionar interface grásfica.
 - Permitir customizar a quantidade máxima de tentativas.
 - Carregar palavras de um arquivo externo.
 - Mostrar um desenho da forca a cada erro.
 - Adicionar dicas de acordo com cada palavra.
