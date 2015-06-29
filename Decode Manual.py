__author__ = 'brodyzt'

orig = ['q','b','w','z','g','h','l','p','x','m','y','u','j','f','r','d','s',' ','t']
new = [' ','i','a','m','t','h','e','s','l','y','n','o','g','u','c','v','w','r','d']

text = raw_input("Please enter the text to decrypt: ")
newText = ''

for char in text: #uses 'orig' and 'new' to exchanged encyrypted letters for decrypted ones
    if char in orig:
        newText = newText + new[orig.index(char)]
    else:
        newText = newText + char

print(newText)