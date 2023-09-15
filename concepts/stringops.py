# The + Operator
# The + operator concatenates strings. It returns a string consisting of the operands joined together, as shown here:
s = 'foo'
t = 'bar'
u = 'baz'
print("Concatenating two strings")
print(s+t)
print(s+t+u)

# The * Operator
# The * operator creates multiple copies of a string. If s is a string and n is an integer,
# either of the following expressions returns a string consisting of n concatenated copies of s:
s = 'foo.'
print(s*4)
print(4*s)
# The multiplier operand n must be an integer. You’d think it would be required to be a positive integer,
# but amusingly, it can be zero or negative, in which case the result is an empty string
print('foo'*-8)

# The in Operator
# Python also provides a membership operator that can be used with strings. The in operator returns
# True if the first operand is contained within the second, and False otherwise
s = 'foo'
print(s in 'That\'s food for thought.')
print(s in 'That\'s good for now.')
# There is also a not in operator, which does the opposite:
print('z' not in 'abc')
print('z' not in 'xyz')

# Built-in string functions
# Function                    Description
# chr()                         Converts an integer to character
# ord()                         Converts a character to an integer
# len()                         Returns the length of a string
# str()                         Returns a string representation of an object

# ord(c) - Returns the integer value of a given character
# At the most basic level, computers store all information as numbers. To represent character data,
# a translation scheme is used which maps each character to its representative number.
#
# The simplest scheme in common use is called ASCII. It covers the common Latin characters you
# are probably most accustomed to working with. For these characters, ord(c) returns the ASCII value for character c:
print(ord('a'))
print(ord('#'))

# chr(n)  - Returns a character for a given integer
# chr() does the reverse of ord(). Given a numeric value n, chr(n) returns a string
# representing the character that corresponds to n:
print(chr(97))
print(chr(35))

# len(s)  - Returns the length of a string
s = 'I am a string.'
print(len(s))

# str(obj)    - Returns a string representation of an object
print(str(49.2))
print(str(3+4j))
print(str(3 + 29))
print(str('foo'))

# String indexing
# Often in programming languages, individual items in an ordered set of data can be accessed directly using a numeric
# index or key value. This process is referred to as indexing. In Python, strings are ordered sequences of character data, and thus can be indexed in
# this way. Individual characters in a string can be accessed by specifying the string name followed by a number in square brackets ([]).
# String indexing in Python is zero-based: the first character in the string has index 0,
# the next has index 1, and so on. The index of the last character will be the length of the string minus one.
s = 'foobar'
print(s[0])
print(s[1])
print(s[3])
print(len(s))
print(s[len(s)-1])

# Here are some examples of negative indexing:
s = 'foobar'
print(s[-1])
print(s[-2])
print(len(s))
print(s[-len(s)])

# String slicing
# Python also allows a form of indexing syntax that extracts substrings from a string,
# known as string slicing. If s is a string, an expression of the form s[m:n] returns the portion of s
# starting with position m, and up to but not including position n
s = 'foobar'
print(s[2:5])
# If you omit the first index, the slice starts at the beginning of the string. Thus, s[:m] and s[0:m] are equivalent:
s = 'foobar'
print(s[:4])
print(s[0:4])
# if you omit the second index as in s[n:], the slice extends from the first index through the end of the string
s = 'foobar'
s[2:]
s[2:len(s)]
# Omitting both indices returns the original string, in its entirety. Literally. It’s not a copy,
# it’s a reference to the original string:
s = 'foobar'
t = s[:]
id(s)
id(t)
print(s is t)
# If the first index in a slice is greater than or equal to the second index, Python returns an empty string.
# This is yet another obfuscated way to generate an empty string, in case you were looking for one:
print(s[2:2])
print(s[4:2])
# Negative indices can be used with slicing as well. -1 refers to the last character, -2 the second-to-last, and so on,
# just as with simple indexing. The diagram below shows how to slice the substring 'oob' from the string 'foobar'
# using both positive and negative indices:
s = 'foobar'
s[-5:-2]
s[1:4]
print(s[-5:-2] == s[1:4])
# Specifying a stride in a string slice
# There is one more variant of the slicing syntax to discuss. Adding an additional : and a third index designates a
# stride (also called a step), which indicates how many characters to jump after retrieving each character in the slice.
# For example, for the string 'foobar', the slice 0:6:2 starts with the first character and ends with the
# last character (the whole string), and every second character is skipped.
s = 'foobar'
# -6 -5 -4 -3 -2 -1
#  f  o  o  b  a  r
#  1  2  3  4  5  6
print(s[0:6:2])
print(s[1:6:2])
# As with any slicing, the first and second indices can be omitted, and default to the first and last characters respectively
s = '12345' * 5
# 1 2 3 4 5 1 2 3 4 5 1  2  3  4  5  1  2  3  4  5  1  2  3  4  5
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
print(s[::5])
print(s[4::5])
# Reversing a string
s = 'foobar'
print(s[::-1])

# Interpolating variables into a string
# In Python version 3.6, a new string formatting mechanism was introduced. This feature is formally
# named the Formatted String Literal, but is more usually referred to by its nickname f-string.
n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

# Replace a character within a string
s = 'foobar'
s = s.replace('b', 'x')
print(s)
# If the optional <count> argument is specified, a maximum of <count> replacements are performed, starting at the left end of s:
s = 'foo bar foo baz foo qux'
print(s.replace('foo','grault',2))

# Built-in string methods
# capitalize() - Capitalizes the target string
s = 'foO BaR BAZ quX'
print(s.capitalize())
# lower() - converts alphabetic character to lower case
# s.lower() returns a copy of s with all alphabetic characters converted to lowercase:
s = 'FOO Bar 123 baz qUX'
print(s.lower())
# upper() - returns a copy of s with alphabetic characters converted to upper case
s = 'FOO Bar 123 baz qUX'
print(s.upper())

# isupper() - Determines whether the target string’s alphabetic characters are uppercase.
print('ABC'.isupper())
print('ABC1$D'.isupper())
print('Abc1$D'.isupper())
# islower() - Determines whether the target string’s alphabetic characters are lowercase.
print('ABC'.islower())
print('ABC1$D'.islower())
print('abc1$d'.islower())

# Strip - remove whitespaces from a string
s = '          Hello World               '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# Split - breaking a string based on a parameter and storing the substrings as a part of list
s = 'Hello World'
print(s.split(' '))

# startswith - Determines whether the target string starts with the given substring
# When you use the Python .startswith() method, s.startswith(<suffix>) returns True if s starts with the s
# pecified <suffix> and False otherwise
print('foobar'.startswith('foo'))
print('foobar'.startswith('bar'))

# endswith - Determines whether the target string ends with a given substring.
# When you use the Python .endswith(<suffix>) returns True if s ends with the
# specified <suffix> and False otherwise:
print('foobar'.endswith('foo'))
print('foobar'.endswith('bar'))
