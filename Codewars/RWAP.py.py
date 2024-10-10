'''In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.'''


def alphabet_position(text):
    text = text.lower()  # Convert the text to lowercase
    lst = list(text)
    stack = []
    for letter in lst:
        if letter in alphabet:
            print(alphabet[letter])
            stack.append(str(alphabet[letter]))

    result = ' '.join(stack)
    return result

alphabet = {}    
for i, letter in enumerate('abcdefghijklmnopqrstuvwxyz', start=1):
    alphabet[letter] = i

text = "The sunset sets at twelve o' clock."
task = alphabet_position(text)
print(task)