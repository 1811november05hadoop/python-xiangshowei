#!/usr/bin/env python3

import re
import math
import os

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
	print(acronym("Complementary metal-oxide semiconductor"))
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
	
	print("---Testing calculate_prime_factors()---")
	try:
		print(calculate_prime_factors(1))
	except AssertionError:
		print("1 is not a prime number")
	print(calculate_prime_factors(2))
	print(calculate_prime_factors(49))
	print()	

	print("---Testing is_pangram()---")
	print(is_pangram("The quick brown fox jumps over the lazy dog!@#$%^&"))
	print()

	print("---Testing sort()---")
	print(sort([2,4,5,1,3,1]))
	print()
	
	print("---Testing rotate()---")
	print(rotate(26, "The quick brown fox jumps over the lazy dog."))
	print(rotate(13, "The quick brown fox jumps over the lazy dog."))
	print(rotate(53, "The quick brown fox jumps over the lazy dog."))
	print()
	
	print("---Testing store_even_and_odd_numbers()---")
	store_even_and_odd_numbers()
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
		#get the individual digits of the number
		digits = [int(num) for num in str(number)]
		num_digits = len(digits)
		
		for digit in digits:
			digit_sum += digit ** num_digits
		
		return digit_sum == number
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def calculate_prime_factors(number):
	assert (type(number) == int)
		
	assert number != 1
	
	prime_factors = []
	if number == 2 or number == 3:
		prime_factors.append(number)
		
		return prime_factors
	else:
		num_is_even = number % 2 == 0
		
		if num_is_even:
			#get all 2's that make up the prime factorization
			while num_is_even:
				prime_factors.append(2)
				number = number / 2
				#parity of the expression needs to be updated because the value of number is being updated
				num_is_even = number % 2 == 0
		
		#getting the odd prime factors
		for i in range (3, int(math.sqrt(number) + 1), 2):
			while number % i == 0:
				prime_factors.append(i)
				number = number / i
		
		#getting the last prime factor if applicable
		if number > 2:
			prime_factors.append(int(number))
		
		return prime_factors
		
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def is_pangram(sentence):
	assert (type(sentence) == str)

	alphabetSet = set()
	
	for ch in sentence:
		if ch.isalpha():
			if ch.isupper():
				ch = ch.lower()
			alphabetSet.add(ch)
	
	return len(alphabetSet) == 26
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.

param: list
return: list
'''
def sort(numbers):
	assert (type(numbers) == list)

	for i in range(0, len(numbers)):
		min_index = i

		for j in range (i + 1, len(numbers)):
			#find the index of the smallest number
			if numbers[j] <= numbers[min_index]:
				min_index = j

		#swap element at min_index to the front of the list 
		#but only if the element is out of order to avoid unncessary swap executions
		if(min_index != i):
			swap(numbers, i, min_index)
	
	return numbers

def swap(array, index1, index2):
	temp = array[index1]
	array[index1] = array[index2]
	array[index2] = temp 
'''
9. Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.
 
The general notation for rotational ciphers is ROT + <key>. 
The most commonly used rotational cipher is ROT13.
	  
A ROT13 on the Latin alphabet would be as follows: 
- Plain: abcdefghijklmnopqrstuvwxyz
- Cipher: nopqrstuvwxyzabcdefghijklm  

It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.
Cipher text is written out in the same formatting as the input including spaces and punctuation. 

Examples: 
- ROT5 omg -> trl 
- ROT0 c -> c 
- ROT26 Cool -> Cool 
- ROT13 The quick brown fox jumps over the lazy dog. -> Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
- ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. -> The quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
	assert (type(key) == int)
	assert (type(string) == str)

	if key == 0 or key == 26:
		return string
	else:
		while key > 26:
			key = key - 26
		
		alphabet = "abcdefghijglmnopqrstuvwxyz"
		encoded_string = []

		for ch in string:
			if ch.isalpha():
				replacement_character_index = 0
				replacement_character = ""

				if ch.isupper():
					# ASCII math done via the ord() function
					
					# Extracting the correct character from the alphabet String 
					# and replacing it with its corresponding character
					# To make sure the index of character we're trying to extract from the 
					# alphabet String stays within bounds, the numerical value 
					# of the character of "A" or "a" needs to be subtracted depending on its case
					# from the character being examined
					replacement_character_index = ord(ch) - ord("A") + key
					
					if replacement_character_index >= len(alphabet):
						replacement_character_index = replacement_character_index - len(alphabet)
					replacement_character = alphabet[replacement_character_index].upper()

				else:
					replacement_character_index = ord(ch) - ord("a") + key

					if replacement_character_index >= len(alphabet):
						replacement_character_index = replacement_character_index - len(alphabet)
					replacement_character = alphabet[replacement_character_index]
				
				encoded_string.append(replacement_character)
			
			#add non-letters as is
			else:
				encoded_string.append(ch)

		return "".join(encoded_string)

'''	
10. Take 10 numbers as input from the user 
and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none; receive user input from keyboard
return: nothing 
'''
def store_even_and_odd_numbers():
	# open() will check if the file already exists.
	# If "w" mode is selected, the existig file will be truncated
	# and the first write() functional call will overwrite the existing file
	# while subsequent write() calls will append to file 

	# Note: if using ## with open("file_name", "w") as variable_name: ## 
	# the write() call will close the file; use open() if writing to a file
	# multiple times and close the file explictly when done
	even_number_file = open("evenNumbers.txt", "w")
	odd_number_file = open("oddNumbers.txt", "w")

	print("Please enter a number: ")
	start_counter = 1
	stop_counter = 10
	while start_counter <= stop_counter:		
		user_input = input()

		if type(int(user_input)) != int:
			raise ValueError

		else:
			number = int(user_input)
		  	
			if number % 2 == 0:
				even_number_file.write(str(number) + "\n")
			
			else:
				odd_number_file.write(str(number) + "\n")
			
		start_counter = start_counter + 1

	str(even_number_file.seek(0,2)).rstrip()
	str(odd_number_file.seek(0,2)).rstrip()

	even_number_file.close()
	odd_number_file.close()
	
if __name__ == "__main__":
	main()
