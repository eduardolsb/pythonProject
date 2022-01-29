import random
import playsound

choosennumber = random.randint(1, 5)

endgame = 0

pontos = 5

qualidade = ['BURRO', 'BESTA', 'MEIA PATACA', 'MENINO BAUM', 'MISERAVI']

while endgame == 0:

    numero = input('Escolha um número entre 1 e 5: ')

    if numero.isnumeric() and 6 > int(numero) > 0:

        if choosennumber == int(numero):
            playsound.playsound("D:/PYTHONPROJECTS/FIRSTPROJECT/APPLICACAO/mp3/certo.mp3")
            print(f'Acertou miseravi. Sua pontuação é {pontos} tu é {qualidade[pontos - 1]} mininu')
            endgame = 1
        else:
            playsound.playsound("D:/PYTHONPROJECTS/FIRSTPROJECT/APPLICACAO/mp3/errou.mp3")
            print(f'Errrrrrroooooou.')
            pontos = pontos - 1
    else:

        print('Digita um numero miseravi')