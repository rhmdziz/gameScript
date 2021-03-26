import random
def bgk():
    # intro
    print('BATU KERTAS GUNTING MELAWAN BOT')
    element = ['batu','gunting','kertas']
    bot = random.choice(element)
    print('b = batu\nk = kertas\ng = gunting')
    ply = str(input('Masukan pilihanmu (b/k/g): '))
    
    # konversi
    if ply == 'b' or ply == 'B':
        ply = 'batu'
    elif ply == 'k' or ply == 'K':
        ply = 'kertas'
    elif ply == 'g' or ply == 'G':
        ply = 'gunting'
    else:
      	print('masukkan opsi yang benar\n')
    	  
    menang = '=> selamat anda menang\n'
    kalah  = '=> maaf anda kalah\n'
    
    # algoritma batu gunting kertas
    if bot == ply:
        print(ply,'vs',bot)
        print('=> s e r i\n')
        
    elif bot == 'batu' and ply == 'kertas':
    	  print(ply,'vs',bot)
    	  print(menang)
    elif bot == 'gunting' and ply == 'batu':
    	  print(ply,'vs',bot)
    	  print(menang)
    elif bot == 'kertas' and ply == 'gunting':
    	  print(ply,'vs',bot)
    	  print(menang)
    
    elif bot == 'kertas' and ply == 'batu':
    	  print(ply,'vs',bot)
    	  print(kalah)
    elif bot == 'batu' and ply == 'gunting':
    	  print(ply,'vs',bot)
    	  print(kalah)
    elif bot == 'gunting' and ply == 'kertas':
    	  print(ply,'vs',bot)
    	  print(kalah)
    	  
    # looping
    loop = str(input('mulai lagi? y/n: '))
    if loop == 'y' or loop == 'Y':
    	  bgk()
    else:
    	print('terima kasih')
bgk()
