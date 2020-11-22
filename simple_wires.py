def simple_wires():
	wires_input = input("Enter the wire colors separated by spaces: ").strip().lower().split(" ")
	num_wires = len(wires_input)
	wires = convert_colors(wires_input);

	if num_wires == 3:
		three_wires(wires)
	else:
		serial_number = int(input("Last digit of serial number: "))
		if num_wires == 4:
			four_wires(wires, serial_number)
		elif num_wires == 5: 
			five_wires(wires, serial_number)
		elif num_wires == 6: 
			six_wires(wires, serial_number)
		else:
			print("Bad input!")

	print("\n")

def convert_colors(wires_array):
	red = ["r", "red"]
	white = ["w", "white"]
	blue = ["blu", "blue"]
	black = ["blk", "bla", "black"]
	yellow = ["y", "yellow"]

	wires_array = ["r" if x in red else x for x in wires_array]
	wires_array = ["w" if x in white else x for x in wires_array]
	wires_array = ["blu" if x in blue else x for x in wires_array]
	wires_array = ["blk" if x in black else x for x in wires_array]
	wires_array = ["y" if x in yellow else x for x in wires_array]

	return wires_array

def three_wires(wires):
	if "r" not in wires:
		print("Cut the 2nd wire!")
	elif wires[-1] == "w": 
		print("Cut the last wire!")
	elif wires.count("blu") > 1:
		print("Cut the last blue wire!")
	else:
		print("Cut the last wire!")


def four_wires(wires, serial_number):
	if wires.count("r") > 1 and serial_number % 2 == 1:
		print("Cut the last red wire!")
	elif wires[-1] == "y" and "r" not in wires:
		print("Cut the first wire!")
	elif wires.count("blu") == 1:
		print("Cut the first wire!")
	elif wires.count("y") > 1:
		print("Cut the last wire!")
	else:
		print("Cut the second wire!")

def five_wires(wires, serial_number):
	if wires[-1] == "blk" and serial_number % 2 == 1:
		print("Cut the fourth wire!")
	elif wires.count("r") == 1 and wires.count("y") > 1:
		print("Cut the first wire!")
	elif wires.count("blk") == 0:
		print("Cut the second wire!")
	else:
		print("Cut the first wire!")
	
def six_wires(wires, serial_number):
	if wires.count("y") == 0 and serial_number % 2 == 1:
		print("Cut the third wire!")
	elif wires.count("y") == 1 and wires.count("w") > 1:
		print("Cut the fourth wire!")
	elif wires.count("r") == 0:
		print("Cut the last wire!")
	else:
		print("Cut the fourth wire!")

if __name__=="__main__":
	simple_wires()