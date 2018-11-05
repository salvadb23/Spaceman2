import random	

words = ["awesome", "cool", "interesting", "microwave", "toaster", "blender"]

random.shuffle(words)

answer = words[1]

display = []
display.extend(answer)

for i in range(len(display)):
	display[i] = "_"

print("Welcome to Spaceman\n")


print ' '.join(display)
print "\n\n\n\n"

count = 0

while count < len(answer):

	guess = raw_input("Guess a letter: ")

	guess = guess.upper

	for i in range(len(answer)):
		if answer[i] == guess:
			display[i] = guess
			count += 1

	print ' '.join(display)
	print "\n\n\n"

print "You win!"