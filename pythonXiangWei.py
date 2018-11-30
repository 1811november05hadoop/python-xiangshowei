#!/usr/bin/env python3

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
	print(reverse("revature"))

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
	
	reversedString = []
	for index in range(len(string) - 1, -1, -1):
		reversedString.append(string[index])
	
	return "".join(reversedString)

	'''
	Solution using slice()
	#not passing an argument for "end" for slice()  will continue until the end of the iterable	
	return string[len(string)::-1]
	'''
if __name__ == "__main__":
	main()
