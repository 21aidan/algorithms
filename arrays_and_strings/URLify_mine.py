def URLify(s, length):
    url = ""
    counter = 0
    for subword in s.split():
        if counter >= (len(s.split()) - 1):
            url = url + subword
        else:
            url = url + subword + '%20'
        counter += 1
    return url

def URLify_best(s, true_length):
    # Count the number of spaces
    space_count = s[:true_length].count(' ')
    
    # Calculate the new length of the string
    new_length = true_length + space_count * 2
    
    # Convert string to list for in-place modification
    char_list = list(s)
    
    # Traverse the string from right to left
    index = new_length - 1
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[index - 2:index + 1] = '%20'
            index -= 3
        else:
            char_list[index] = char_list[i]
            index -= 1
    
    # Convert the list back to string and return
    return ''.join(char_list[:new_length])


input_string = 'hey my name is aidan            '
input_length = 28

print(URLify(input_string, input_length))
print(URLify_best(input_string, input_length))