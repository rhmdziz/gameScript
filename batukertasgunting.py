import random
def bgk():
    print('BATU KERTAS GUNTING')
    bgk = ['batu','gunting','kertas']
    bot = random.choice(bgk)
    print('b = batu\nk = kertas\ng = gunting')
    ply = str(input('Masukan pilihanmu (b/k/g): '))
    if ply == 'b':
        ply = 'batu'
    elif ply == 'k':
        ply = 'kertas'
    elif ply == 'g':
        ply = 'gunting'
    if bot == ply:
        print(ply,'\nvs\n',bot)
        print('S e r i')
    elif 
bgk()

# bentar gan bikin algonya dulu
