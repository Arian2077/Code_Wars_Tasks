def reverse_words(text):
    # Split the text into words, preserving spaces
    words = text.split(' ')
    
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together
    return ' '.join(reversed_words)