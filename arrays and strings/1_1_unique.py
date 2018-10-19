'''

Implement an algorithm to determine if a string has all unique characters. What if you cannot use 
additional data structures?

Boolean Type of function?
time complexity O(n)?
'''

def unique_char(string):
    string_set = set()
    string_list = list(string)
    for char in string_list:
        if char not in string_set:
            string_set.add(char)
            print(char)
        else:
            return False
    return True

x = 'testing'
print(unique_char(x))
