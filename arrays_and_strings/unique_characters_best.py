def isUniqueChars(str):                                                                     # O(n) time
    # check the length of the array doesn't exceed the number of possible characters        # O(1) space
    if len(str) > 128:  # assuming ascii with 128 possible characters
        return false 
    # initialise a list of False booleans
    char_set = [False] * 128    # assuming ascii with 128 possible characters

    # go through the string and call the corresponding boolean true
    str_arr = list(str)
    for char in str:
        # get the ASCII value of the character
        val = ord(char)
        # if one of the booleans is already true, it's already been in the string, so return false
        if char_set[val]:
            return False
        # mark the character as seen    
        char_set[val] = True
    return True

print(isUniqueChars('helo'))