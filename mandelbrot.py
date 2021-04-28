from PIL import Image
import math
import threading
import random

#Create new image
img = Image.new(size=(500, 500), mode='RGB', color=(0, 0, 0))

#Initialize constants
INDENT = (250, 250)
DIVIDER = 150

def checkComplexNum(num):
	newNum = 0
	#50 iterations
	for i in range(50):
		#Mandelbrot fractal formula
		newNum = newNum*newNum + num

		#If complex number is very large, that not included in the set
		if math.isnan(newNum.real):
			img.putpixel((round(num.real*DIVIDER + INDENT[0]), round(num.imag*150 + INDENT[1])), (0, min(i*10, 255), 0))
			return False

	#If complex num did not go to infinity, draw it
	img.putpixel((int(num.real*DIVIDER + INDENT[0]), int(num.imag*DIVIDER + INDENT[1])), (0, 0, 0))

#Function check chuncks 50x50 pixels
def thradFunction(addX, addY):
	for x in range(50):
		for y in range(50):
			checkComplexNum(complex((x + addX - INDENT[0])/DIVIDER, (y + addY - INDENT[1])/DIVIDER))

#Cycles start multi threading
for x in range(10):
	for y in range(10):
		threading.Thread(target=thradFunction, args=(x*50, y*50)).start()
	
	print(f'{(x+1)*10}%')

img.save(f'fractal{random.randint(0, 50)}.png')
img.show()