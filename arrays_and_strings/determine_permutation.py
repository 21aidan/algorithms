def check_permutation(s1, s2):                                                                          # O(n) time
    # check if they're not the same length, as if not they can't be permutations of one another         # O(?) space
    if len(s1) != len(s2):
        return False

    # create an empty list of 0s the length of the ASCII alphabet
    letters_list = [0] * 128

    # go through the first string, find the ASCII value of each character and increment the corresponding index in the letters list
    for char in s1:
        letters_list[ord(char)] += 1

    # go through the second string, find the ASCII value of each character and decrement the corresponding index in letters_list
    for char in s2:
        letters_list[ord(char)] -= 1
        # if the letters list has any characters with less than 0, they can't be permutations as they are already  
        # confirmed to be the same length
        if letters_list[ord(char)] < 0:
            return False
    
    return True

s1 = "hello"
s2 = "hoooo"

print(check_permutation(s1, s2))
