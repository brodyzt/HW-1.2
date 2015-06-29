def sortList (list): #uses bubble sort to sort list from smallest to largest
    listSorted = False
    while(listSorted == False):
        listSorted = True
        for x in range(0, len(list) - 1):
            if(list[x] > list[x+1]): # the following code switches adjacent, out of order items in both alphabet and frequency lists
                temp = list[x+1]
                tempAlph = alphabet[x+1]
                list[x+1] = list[x]
                alphabet[x+1] = alphabet[x]
                list[x] = temp
                alphabet[x] = tempAlph
                listSorted = False #marks the list as not sorted if the program can't cycle through the whole list without finding elements out of order

def contentsOfFile(file): #returns the contents of a file in a string
    tempString = ''
    contents = file.readlines() #returns contents of file in list format with each line of text as object in list
    for line in contents:
        tempString = str(tempString) + str(line) #add each line of text to the temporary string
    return tempString

print("Before continuing with the program, enter the plain English text into the 'Plain Text' file and enter the encrypted text into 'Plain Text'")
while(raw_input("Type 'done' and hit enter once completed: ") != 'done'):
    pass


originalChar = [] #order of character frequency in encrypted text
newChar = [] #order of character frequency in plain english text


for x in range(2):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']

    #opens both files and stores their contents in strings
    if(x == 0):
        text = contentsOfFile(open('Plain Text', 'r'))
    else:
        text = contentsOfFile(open('Encrypted Text', 'r'))
    frequencies = []

#find the frequency of each character and appends them to the corresponding lists
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
        translatedText = translatedText + originalChar[newChar.index(char)] #appends the correct character to the decrypted text using the encryption key

print('\nDecrypted Text: ' + translatedText) #prints the decrypted text