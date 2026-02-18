translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}


def translator(language):
    # Get the dictionary for the specified language
    language_set = translations.get(language)

    def translate_word(word):  # Define the inner function that will perform the translation
        if language_set:  # Check if the language is supported
            return language_set.get(word, f"No translation for '{word}' in {language}")
        else:
            return f"Language '{language}' is not supported."
    return translate_word


translate_to_spanish = translator('spanish')
print(translate_to_spanish('goodbye'))  # Output: adiós


"""
If you're on Duolingo, this exercise is for you! 🦉

Let's use higher-order functions to translate some common phrases from different languages.

First, define a translator() function that takes a single language parameter.

Inside the function, add a translations dictionary that contains translations for common phrases in different languages:

translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}

Next, define an inner translate_word() function that takes a word parameter and returns a translation if the word exists in a specific language.

Return the inner translate_word() function from the outer translator() function.

Finally, let's test our translator() function with different languages:

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola

Have fun, maybe try a new language!
"""
