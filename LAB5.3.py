numbers = []

def average():
	while len(numbers) == 0 or numbers[-1] != 0:
		floatNumber = float(raw_input('Enter a number: '))
		numbers.append(floatNumber)
		
	theAVG = sum(numbers) / (len(numbers) -1)
	print theAVG

average()