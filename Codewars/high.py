<<<<<<< HEAD
def high(x):
    # Split the input string into words
    words = x.split()
    
    # Initialize variables to keep track of the highest scoring word and its score
    highest_score = 0
    highest_word = ""
    
    # Iterate through each word
    for word in words:
        # Calculate the score for the current word
        score = sum(alphabet_dict[char.lower()] for char in word if char.lower() in alphabet_dict)
        
        # Check if this word has the highest score
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word

# Alphabet dictionary
alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

# Test the function with a sample sentence
sentence = "Hello my name is jack marston"
=======
def high(x):
    # Split the input string into words
    words = x.split()
    
    # Initialize variables to keep track of the highest scoring word and its score
    highest_score = 0
    highest_word = ""
    
    # Iterate through each word
    for word in words:
        # Calculate the score for the current word
        score = sum(alphabet_dict[char.lower()] for char in word if char.lower() in alphabet_dict)
        
        # Check if this word has the highest score
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word

# Alphabet dictionary
alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

# Test the function with a sample sentence
sentence = "Hello my name is jack marston"
>>>>>>> 8267eb5b08f297691c348ec76d94ab0d97dd17ed
print(high(sentence))  # Output will be the word with the highest score