
import sys

import numpy as np

font_image = []

file_pgm = open(sys.argv[1], "rt")
file_fnt = open(sys.argv[2], "wb")

file_pgm.readline()
file_pgm.readline()
file_pgm.readline()
file_pgm.readline()

for i in range(6144):
	if(int(file_pgm.readline()) > 0):
		font_image.append(True)
	else:
		font_image.append(False)

for y in range(3):
	for x in range(32):
		for i in range(8):
			current_char = 0
			for j in range(8):
				bit_mask = 0x80 >> j
				if(font_image[j + i * 32 * 8 + x * 8 + y * 32 * 8 * 8]):
					current_char = bit_mask | current_char

			file_fnt.write(np.ubyte(current_char))


			

