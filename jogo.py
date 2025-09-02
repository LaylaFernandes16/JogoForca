from random import choice

palavras = [
    'amor', 'vida', 'lua', 'fogo', 'paz', 'sol', 'chuva', 'tempo', 'vento', 'coração',
    'sorriso', 'liberdade', 'força', 'esperança', 'alegria', 'tristeza', 'noite', 'dia',
    'estrela', 'planeta', 'natureza', 'floresta', 'mar', 'montanha', 'caminho', 'luz',
    'escuro', 'fé', 'coragem', 'amizade', 'respeito', 'carinho', 'verdade', 'mentira',
    'silêncio', 'grito', 'poesia', 'verso', 'música', 'dança', 'arte', 'pintura', 'história',
    'guerra', 'paz', 'mundo', 'terra', 'universo', 'galáxia', 'viagem', 'sonho', 'realidade',
    'tempo', 'passado', 'presente', 'futuro', 'segredo', 'medo', 'abraço', 'beijo', 'destino',
    'olhar', 'voz', 'palavra', 'gesto', 'sentimento', 'emoção', 'razão', 'pensamento'
]
palavra = choice(palavras)
qnt_letra = len(palavra)
tentativa = 1
letra_certa = []
letra_errada = []
palavra_correta = []

print("Bem vindo(a) para o jogo da forca!")
tracos = ['_' for i in palavra]
print(' '.join(tracos))

while tentativa <= 6:
    letra = input("Digite uma letra: ").lower()

    if letra in letra_errada or letra in letra_certa:
        print("Você já tentou essa letra, tente novamente!")

    if letra in palavra:
        letra_certa.append(letra)
        for item in range(len(palavra)):
            if palavra[item] == letra:
                tracos[item] = letra
        if "_" not in tracos:
            print("Você venceu!")
            print("Palavra:", palavra)
            break
    else:
        letra_errada.append(letra)
        tentativa += 1
        if tentativa > 6:
            print(f'Suas tentativas acabaram. A palavra era "{palavra}". Boa sorte da próxima vez!')
            break

    print(f'Letras erradas: {", ".join(letra_errada)}')
    print(' '.join(tracos))