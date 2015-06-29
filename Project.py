def sortList (list):
    listSorted = False
    while(listSorted == False):
        listSorted = True
        for x in range(0, len(list) - 1):
            if(list[x] > list[x+1]):
                temp = list[x+1]
                tempAlph = alphabet[x+1]
                list[x+1] = list[x]
                alphabet[x+1] = alphabet[x]
                list[x] = temp
                alphabet[x] = tempAlph
                listSorted = False
def contentsOfFile(file):
    tempString = ''
    contents = file.readlines()
    for line in contents:
        tempString = str(tempString) + str(line)
    return tempString

print("Before continuing with the program, enter the plain English text into the 'Plain Text' file and enter the encrypted text into 'Plain Text'")
while(raw_input("Type 'done' and hit enter once completed: ") != 'done'):
    pass

originalChar = []
newChar = []

for x in range(2):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
    if(x == 0):
        text = contentsOfFile(open('Plain Text', 'r'))
    else:
        text = contentsOfFile(open('Encrypted Text', 'r'))
    frequencies = []

    for char in alphabet:
        frequencies.append(text.count(char))
    sortList(frequencies)
    if(x == 0):
        originalChar = alphabet
    else:
        newChar = alphabet

translatedText = ''
textToDecrypt = contentsOfFile(open('Encrypted Text', 'r'))
for char in textToDecrypt:
    if(char in newChar):
        translatedText = translatedText + originalChar[newChar.index(char)]

print('\nDecrypted Text: ' + translatedText)