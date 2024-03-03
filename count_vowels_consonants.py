"""
Write a program that asks the user for the number of lines for the entered poem.
It then allows the user to enter the desired number of lines.

Then output the number of lines, vowels and consonants in the poem and in each line.

For simplicity, let us enter the poem in small English letters only.

Input example:

How many lines will there be? 4

Once there was an elephant,
Who tried to use the telephant
No! No! I mean an elephone
Who tried to use the telephone

Example result:
Number of vowels: 40
Number of consonants: 51
"""


vowel_list = "aeiou"
consonants_list = "bcdfghjklmnpqrstvwxyz"
vowels = 0
consonants = 0
how_many_lines = input("How many lines will there be?: ")

for i in range(1, int(how_many_lines)+1):
    poem_line = input("Input poem: ")
    for char in poem_line.lower():
        if char in vowel_list:
            vowels += 1
        elif char in consonants_list:
            consonants += 1

print(f"Number of vowels: {vowels}\nNumber of consonants: {consonants}")
