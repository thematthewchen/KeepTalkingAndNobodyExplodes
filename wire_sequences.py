def wire_sequences():
	wire_count = 1
	red_count = 0
	blue_count = 0
	black_count = 0

	red_table = ["C", "B", "A", "AC", "B", "AC", "ABC", "AB", "B"]
	blue_table = ["B", "AC", "B", "A", "B", "BC", "C", "AC", "A"]
	black_table = ["ABC", "AC", "B", "AC", "B", "BC", "AB", "C", "C"]

	while True:
		cut = False
		wire_input = input("Wire " + str(wire_count) + ": ").strip().lower().split()
		color = wire_input[0]
		letter = wire_input[1].upper()

		if color == "red":
			if letter in red_table[red_count]:
				cut = True
			red_count += 1
		elif color == "blue":
			if letter in blue_table[blue_count]:
				cut = True
			blue_count += 1
		else:
			if letter in black_table[black_count]:
				cut = True
			black_count += 1

		if cut:
			print("\nCUT\n")
		else:
			print("\nDON'T CUT\n")
		wire_count += 1
		
if __name__=="__main__":
	wire_sequences()