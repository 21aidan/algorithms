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

print(URLify('hey my name is aidan', 28))