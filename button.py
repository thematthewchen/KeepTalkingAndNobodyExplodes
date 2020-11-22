def button():
	color = input("Button color (full name): ").strip().lower()
	text = input("Button text: ").strip().lower()
	batteries = int(input("Number of batteries: "))
	print("\n")

	if color == "blue" and text == "abort":
		releasing_held_button()
	elif batteries > 1 and text == "detonate":
		print("Press and immediately release the button!")
	else:
		is_lit_CAR = input("Is there a lit indicator with label CAR? ").strip().lower()
		if color == "white" and is_yes(is_lit_CAR):
			releasing_held_button()
		else:
			is_lit_FRK = input("Is there a lit indicator with label FRK? ").strip().lower()
			if batteries > 2 and is_yes(is_lit_FRK):
				print("Press and immediately release the button!")
			elif color == "yellow":
				releasing_held_button()
			elif color == "red" and text == "hold":
				print("Press and immediately release the button!")
			else:
				releasing_held_button()
	print("\n")

def is_yes(input):
	return input in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

def releasing_held_button():
	print("Hold the button...")
	color_held = input("Color of strip (full name): ").strip().lower()
	print("\n")
	if color_held == "blue":
		print("Release when countdown timer has 4 in any position!")
	elif color_held == "white":
		print("Release when countdown timer has 1 in any position!")
	elif color_held == "yellow":
		print("Release when countdown timer has 5 in any position!")
	else:
		print("Release when countdown timer has 1 in any position!")

if __name__=="__main__":
	button()