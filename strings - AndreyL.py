"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

# 1. Create a function that returns a sorted string with no duplicate characters (keep any whitespace): Example: ' cfghilmnoprstuy'
def no_duplicates(a_string):
    b_string=""
    list_string = sorted(a_string)
    for i in list_string:
        if i not in b_string:
            b_string=b_string + i

    return(b_string)



#2. Create a function that returns the words in reverse order: Example: ['circus', 'flying', 'pythons', 'monty']
def reversed_words(a_string):
    a_string1=a_string.split()
    return a_string1[::-1]

#3.Create a function that returns a list of 4 character strings: Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
def four_char_strings(a_string):
    k = 0
    list_string= []
    for i in a_string:
        if k<=len(a_string):
            list_string.append(a_string[k:k+4])
            k = k+4
    return list_string




def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    return pytest.main(__file__)


if __name__ == '__main__':
   main()


# a_string ='monty pythons flying circus'
# print(no_duplicates(a_string))
# print(reversed_words(a_string))
# print(four_char_strings(a_string))