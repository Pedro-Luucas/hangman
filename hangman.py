import random
from funcoesUteis import printHangman, linha1, linha2




# lista de palavras de acordo com a dificuldade
palavrasFacil = ['casa', 'sol', 'gato', 'rio', 'bolo', 'flor', 'mao', 'pao', 'rato', 'lua']
palavrasMedio = ['computador', 'aventura', 'chocolate', 'elefante', 'guitarra', 'palavra', 'viagem', 'tesouro', 'amizade', 'felicidade']
palavrasDificil = ['xadrez', 'enigma', 'criptografia', 'labirinto', 'xerife', 'xilogravura', 'quimica', 'astronomia', 'jazz', 'xenofobia']

# loop principal do jogo
while True:
    linha2()
    print('JOGO DE HANGMAN ')
    linha2()
    try:
        # escolha de dificuldade (a prova de erros)
        while True:
            dif = int(input('QUAL A DIFICULDADE? (1 para fácil, 2 para médio e 3 para difícil)\n'))
            if dif < 1 or dif > 3:
                linha1()
                print('escolha um número válido! ')
                linha1()
                continue
            else:
                break
    except:
        linha1()
        print('escolha um número válido!.')
        linha1()
        break

    # switch case no python!1!!
    match dif:
        case 1:
            palavra = random.choice(palavrasFacil)
            
        case 2:
            palavra = random.choice(palavrasMedio)
            
        case 3:
            palavra = random.choice(palavrasDificil)
            
    # variaveis
    palavraString = '_'*len(palavra)
    erros = 0
    letrasTentadas = [' ']
    
    # loop do jogo com a palavra escolhida e as variaveis definidas
    while palavraString != palavra and erros <= 6:
        letra = str(input('ESCOLHA UMA LETRA: ')).lower().strip()

      # logica do jogo
        if letra in palavra:
            pCaracteres = [*palavraString]
            for i,l in enumerate(palavra):
                if letra == l:
                    pCaracteres[i] = l
            palavraString = ''.join(pCaracteres)
        else:
            letrasTentadas.append(letra)
            erros += 1

        # printar tudo
        linha1()
        printHangman(erros)
        print(palavraString)
        print('LETRAS TENTADAS: ',end='')
        for i in letrasTentadas:
            print(i,end=' ')
        print()
        linha1()

    linha2()
    if erros > 6:
        dnv = str(input('você perdeu. deseja jogar novamente?(s/n) ')).lower().strip()
    else:
        dnv = str(input('parabens!! voce ganhou. deseja jogar novamente?(s/n) ')).lower().strip()
    if dnv == 'n':
        break
    


linha2()
print('obrigado por jogar! ')