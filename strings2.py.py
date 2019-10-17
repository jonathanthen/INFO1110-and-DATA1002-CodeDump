def get_first_lowercase_pair(text):
"""Return the index of the first pair of letters that are both
lowercase in the given string.

 If no such pair exists, or if the argument is not a
 string, return -1."""

Input | Expected Output | Justification
"AAaaAA" | 2 | Simple, Positive Case
#Pair in the middle
"xyz" | 0 | Simple, Positive Case
"AAAAAaAaa" | 7 | Simple, Positive Case
"ABCDefg" | 4 | Simple, Positive Case
"##LoLbb" | 6 | Complicated, Positive Case
#Include non letters
123 | -1 | Simple, Negative Case
# Numbers
"AAaAA" | -1 | Simple, Negative Case
"!@#$" | -1 | Complicated, Negative Case
"" | -1 | Complicated, Negative Case
#input < 2 characters
IndexError | -1 | Invalid type
