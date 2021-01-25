def passwords():
	first_letter = input("Enter the first letters: ")
	second_letter = input("Enter the second letters: ")
	third_letter = input("Enter the third letters: ")
	fourth_letter = input("Enter the fourth letters: ")
	fifth_letter = input("Enter the fifth letters: ")

	file = open("passwords.txt", "r")
	for password in file:
		if (password[0] in first_letter 
			and password[1] in second_letter
			and password[2] in third_letter
			and password[3] in fourth_letter
			and password[4] in fifth_letter):
			print("Password is: " + password)


if __name__=="__main__":
	passwords()