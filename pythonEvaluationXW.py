#!/usr/bin/env python3

import re
'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not suported by Python natively.

8) Don't change the parameters or return types, follow the directions.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print("---Testing reverse()---")
	print(reverse("revature"))
	print()

	print("---Testing acronym()---")
	print(acronym("Portable Network Graphic"))
	print(acronym("Deoxyribo-nucleic acid"))
	print()

	print("---Testing whichTriangle()---")
	print(whichTriangle(5.0,5.0,5.0))
	print(whichTriangle(3.0,3.0,5.5))
	print(whichTriangle(3.0,4.0,5.0))
	print()

	print("---Testing scrabble()---")
	print(scrabble("scrabble"))
	print(scrabble("!@#$%^&*"))
	print(scrabble("mix@!"))
	print()

	print("---Testing is_armstrong_number()---")
	print(is_armstrong_number(8))
	print(is_armstrong_number(153))
	print(is_armstrong_number(154))
	print()
	
	print("---Testing get_prime_factors()---")
	print()
	print()
	
	print("---Testing is_pangram()---")
	print()
	print()
	
	print("---Testing merge_sort()---")
	print()
	print()
	
	print("---Testing rotate_cipher_encode()---")
	print()
	print()
	
	print("---Testing store_even_and_odd_numbers_in_file()---")
	print()
	print()
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	assert type(string) == str
	
	reversed_string = []
	for index in range(len(string) - 1, -1, -1):
		reversed_string.append(string[index])
	
	'''
	Solution using slice()
	#not passing an argument to "end" for slice() will continue until the end of the iterable automatically	
	return string[len(string)::-1]
	'''
	return "".join(reversed_string)

'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):	
	assert type(phrase) == str

	acronym = []
	words = re.split("[ -]", phrase)
	for word in words:
		acronym.append(word[0].capitalize())
	
	return "".join(acronym)

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. 
- An equilateral triangle has all three sides the same length. 
- An isosceles triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) 
- A scalene triangle has all sides of different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	assert type(sideOne) == float
	assert type(sideTwo) == float	
	assert type(sideThree) == float

	triangleType = None
	if sideOne == sideTwo and sideOne == sideThree:
		triangleType = "equilateral"
	elif sideOne != sideTwo and sideOne != sideThree and sideTwo != sideThree:
		triangleType = "scalene"
	else: 
		triangleType = "isosceles"

	return triangleType

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- 
A, E, I, O, U, L, N, R, S, T = 1;
D, G = 2; 
B, C, M, P = 3; 
F, H, V, W, Y = 4; 
K = 5; 
J, X = 8; 
Q, Z = 10; 

Example: "cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	assert type(word) == str

	score = 0
	for ch in word:
		if ch.isalpha:
			if ch.isupper():
				ch.lower()
		
			if ch in "aeioulnrst":
				score += 1
			elif ch in "dg":
				score += 2
			elif ch in "bcmp":
				score +=3
			elif ch in "fhvwy":
				score += 4
			elif ch == "k":
				score += 5
			elif ch in "jx":
				score += 8
			elif ch in "qz":
				score += 10
	return score
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:
- 9 is an Armstrong number, because 9 = 9^1 = 9. 
- 10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 2. 
- 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 
- 154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

param: int
return: bool
'''
def is_armstrong_number(number):
	assert (type(number) == int)
	
	if number < 10:
		return True
	else:
		digit_sum = 0
		#converts an int into a list of int; get the individual digits of the number
		digits = [int(num) for num in str(number)]
		num_digits = len(digits)
		
		for digit in digits:
			digit_sum += digit ** num_digits

		
		return digit_sum == number
		
if __name__ == "__main__":
	main()
