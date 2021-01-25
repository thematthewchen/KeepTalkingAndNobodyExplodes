def complicated_wires():
	print("File Line Format: led color star\n\n")
	file = open("input.txt", "r")

	serial_number = input("Last digit of serial number: ")
	parallel_port = input("parallel port: ")
	batteries = input("# batteries: ")
	print("\n\n")

	for count, line in enumerate(file):
		line_data = line.split()
		led = line_data[0]
		color = line_data[1].lower()
		red = "r" in color
		blue = "b" in color
		star = line_data[2]

		letter = find_letter(is_true(led), red, blue, is_true(star))
		cut = cut_wire(str(letter[0]), int(serial_number), is_true(parallel_port), int(batteries))
		if cut:
			print("[X]", end=" ")
		else:
			print("[ ]", end=" ")
		print("Wire " + str(count + 1) + ": LED " + led + " | COLOR " + color + " | STAR " + star)

	print("\n\n")

def is_true(input):
	return input.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

def find_letter(led, red, blue, star):
	# false = 0, true = 1
	# [led][red][blue][star]
	venn_diagram = [ 
		[ # no led
			[ # not red
				[ # not blue
					["C"], # no star
					["C"] # yes star
				],
				[ # yes blue
					["S"], # no star
					["D"] # yes star
				]
			],
			[ # yes red
				[ # not blue
					["S"], # no star
					["C"] # yes star
				],
				[ # yes blue
					["S"], # no star
					["P"] # yes star
				]
			]
		],
		[ # yes led
			[ # not red
				[ # not blue
					["D"], # no star
					["B"] # yes star
				],
				[ # yes blue
					["P"], # no star
					["P"] # yes star
				]
			],
			[ # yes red
				[ # not blue
					["B"], # no star
					["B"] # yes star
				],
				[ # yes blue
					["S"], # no star
					["D"] # yes star
				]
			]
		]
	]
	return venn_diagram[int(led)][int(red)][int(blue)][int(star)]


def cut_wire(letter, serial_number, parallel_port, batteries):
	cut = False
	if letter == "C":
		cut = True
	elif letter == "S":
		if serial_number % 2 == 0:
			cut = True
	elif letter == "P":
		if parallel_port:
			cut = True
	elif letter == "B":
		if batteries >= 2:
			cut = True
	return cut
	

if __name__=="__main__":
	complicated_wires()