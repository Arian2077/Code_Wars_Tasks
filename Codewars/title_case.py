def title_case(title, minor_words=""):
    # Convert the minor_words to a set for faster look-up and make them all lowercase
    minor_words = set(minor_words.lower().split())
    
    # Split the title into words
    words = title.split()
    
    # Process each word
    result = []
    for i, word in enumerate(words):
        # Capitalize the first word or any word that's not in the minor_words
        if i == 0 or word.lower() not in minor_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    
    # Join the processed words into a single string
    return " ".join(result)
