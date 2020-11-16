#En este proyecto quiero implementar un juego en mi bot
import palabras
import random

y = random.randrange(len(palabras.palabras3))
p = palabras.palabras3[y]

def iniahor():
	print(p)
	cuadro = ['_' for i in range(len(p))]
	z = list(p)
	return cuadro
	return p
	return z

def ahorcado():
	y = 0

	ahor = ['\n \n \n| \n| ','\n| \n| \n| \n| ','___\n| |\n| \n| \n| ','___\n| |\n| o\n| \n| ','___\n| |\n| o\n| ^\n| ','___\n| |\n| o\n| ^\n| ^']

	ronda = 0


	z = list(p)

	while '_' in cuadro:
		x = str(input())
		if x in z and len(x)==1:
			for i in range(z.count(x)):
				y = z.index(x)
				cuadro.pop(y)
				z.pop(y)
				z.insert(y, '')
				cuadro.insert(y, x)
			return(cuadro)
		else:
			return(ahor[ronda])
			ronda += 1
			if ronda == 6:
				break
