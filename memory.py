def memory():
	# 5 stages each with 2 numbers: position pressed then label pressed 
	stage_data = [
	[0, 0], 
	[0, 0], 
	[0, 0], 
	[0, 0], 
	[0, 0]
	]
	# Stage number, Letter, Number
	#P = press button in position #
	#L = press button with label #
	directions = [
	["1P2", "1P2", "1P3", "1P4"],
	["2L4", "1P", "2P1", "1P"],
	["2L", "1L", "3P3", "3L4"],
	["1P", "4P1", "2P", "2P"],
	["1L", "2L", "4L", "3L"],
	]

	for stage_number in range(5):
		print("\n\n --- Stage " + str(stage_number + 1) + " --- ")
		display = int(input("Display is : ")) - 1 # 0 indexed

		next_stage = int(directions[stage_number][display][0]) - 1 # 0 indexed
		letter = directions[stage_number][display][1]

		if stage_number == next_stage: # no need to check previous state
			action_number = directions[stage_number][display][2]
			if letter == "L": 
				print("Press button with label " + str(action_number))
				stage_data[stage_number][0] = int(input("Position of button pressed is: "))
				stage_data[stage_number][1] = action_number
			elif letter == "P": 
				print("Press button in position " + str(action_number))
				stage_data[stage_number][0] = action_number
				stage_data[stage_number][1] = int(input("Label of button pressed is: "))
		else: # check previous state
			if letter == "L":
				action_number = stage_data[next_stage][1] # label of next_stage
				print("Press button with label " + str(action_number))
				#print("Press button with same label as the button you pressed in stage " + str(next_stage + 1) + " : " + str(action_number))
				stage_data[stage_number][0] = int(input("Position of button pressed is: "))
				stage_data[stage_number][1] = action_number
			elif letter == "P":
				action_number = stage_data[next_stage][0] # position of next_stage
				print("Press button in position " + str(action_number))
				#print("Press button with same position as the button you pressed in stage " + str(next_stage + 1) + " : " + str(action_number))
				stage_data[stage_number][0] = action_number
				stage_data[stage_number][1] = int(input("Label of button pressed is: "))


if __name__=="__main__":
	memory()