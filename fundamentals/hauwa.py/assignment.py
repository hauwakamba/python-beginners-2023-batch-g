# For each of the following string methods,
# explain how it works with an example

# 1. find
#find is a method of string that finds the first occurrence of a substring in a string and returns its index
name="aisha,fatima,hauwa"
print(name.find("hauwa"))
place="kebbi,sokoto,zamfara"
print(place.find("kebbi"))

# 2. format
#
# 3. index
#this method is used to assess the individual character by indexing the characters starting from 0 for th first character and goes up from there.

# 4. isalnum
#this method checks if all the characters in a string are alphanumeric.it returns TRUE if all characters are alphanumeric and FALSE if otherwise

# 5. isalpha
#this method checks if all the characters in a string are alphabetic characters.it returns TRUE if all characters are in letters and FALSE if otherwise

# 6. isdecimal
#this method checks if all the characters in a string are decimal digits.it returns TRUE if all characters are in decimal digits and FALSE if otherwise.
age="123456"
sticks='111'

# 7. islower
#this method checks if all characters in the string are in lowercase.it returns TRUE if all characters in the string are in lowercase,and FALSE if otherwise.
flowers="FLOWERS SMELLS NICE"
is_lower=flowers.islower()
print(is_lower)
animals="animals are cute"
is_lower=animals.islower
print(is_lower)

# 8. isupper
#this method checks if all characters in the string are in uppercase.it returns TRUE if all characters in the string are in uppercase,and FALSE if otherwise.
flowers="flowers smells nice"
is_upper=flowers.isupper()
print(is_upper)
animals="Animals Are Cute"
is_upper=animals.isupper
print(is_upper)

# 9. upper
#this method converts a string to an uppercase
shop="milk,milo"
place="market,school"

# 10. lower
#this method converts a string to a lowercase
shop="Milk,Milo"
place="Market,School"

# 11. replace
#this method replaces a substring with another subtring
fruits="animals"
(fruits.replace("animals","human"))
place="kamba fishing festival"
(place.replace("kamba","argungu"))

# 12. split
#is a method of string in it split a string into a list of substrings based on a specified seperator
tools2=("hammer,rake,hoe,")
print(tools2.split(","))
human=("baby,man,lady")
print(human.split(","))

# 13. strip
#this method removes leading and trailing whitespace
human="   animals are cute  "
tools="   hammer are used by carpenters   "

# 14. join
#this methods joins elements of an iterable into a string
hamun="baby   ,plants,   animals  "
animals="panda,   goat"

# 15. istitle
#this method is used to check if a string is in title case this meaning each word in a string begins with an uppercase and the rest of the letters in lowercase
place="Kebbi Is Nice"
countries="uganda,ghana,niger"