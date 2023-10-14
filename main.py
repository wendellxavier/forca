palavra = "goblin"
letras_usuario = []
chances = 4
ganhou = False


while True:
    for letra in palavra:
        if letra.lower()  in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
        print("")
    tentativas = input("Escolha uma letra para adivinhar a palvra: ")
    letras_usuario.append(tentativas.lower())

    if tentativas.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break
    
    print(f"voce tem {chances} chances!")

if ganhou:
    print(f"Você ganhou, apalavra era: {palavra}")
else:
    print(f"Você perdeu, a palavra era: {palavra}")