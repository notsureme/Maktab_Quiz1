def read_file(filename):
    with open(filename, "r") as file:
        text = file.read()
    return text

def duplicate_word_gen(text):
    char = ''
    words =""

    for word in text.split(' '):
        temp = {}
        words = ""
        for element in word:
            if element in temp:
                temp[element] +=1
            else:
                temp[element] = 1
            if temp[element] > 1:
                words = word
    yield words

text = read_file('text.txt')
count = len(text)

while count > 1:
    print(next(duplicate_word_gen(text)))
    count -= 1