import random
from funcoesUteis import printHangman, linha1, linha2




# lista de palavras de acordo com a dificuldade
palavrasFacil = []
palavrasMedio = []
palavrasDificil = []

while True:
    while True:
        print('JOGO DE HANGMAN ')
        linha2()
        try:
            while True:
                dif = int(input('QUAL A DIFICULDADE? (1 para fácil, 2 para médio e 3 para difícil)\n'))
                if dif < 1 or dif > 3:
                    print('escolha um número válido! ')
                    continue
                else:
                    break
        except:
            print('escolha um número válido!.')
            break


        match dif:
            case 1:
                palavra = random.choice(palavrasFacil)
                break
            case 2:
                palavra = random.choice(palavrasMedio)
                break
            case 3:
                palavra = random.choice(palavrasDificil)
                break

        
        