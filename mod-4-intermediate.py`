'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_let(let, shift):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_len = len(alph)

    let_index = alph.index(let)

    shifted_index = (let_index + shift) % alph_len
    
    return alph[shifted_index]

print(shift_let("A", 12))
print(shift_let("A", 0)) 
print(shift_let("A", 2))
print(shift_let("Z", 1)) 
print(shift_let("X", 5))

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def caesar_cipher(message, shift):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    alph_len = len(alph)

    encoded_message = ''

    for letters in message:
        letters_index = alph.index(letters)

        shifted_index = (letters_index + shift) % alph_len

        encoded_message += alph[shifted_index]

    return encoded_message


message=input("Input the message:")
shift=int(input("Input the number by which to shift the letters:"))
print(caesar_cipher(message, shift)) 


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    def shift_by_letter(letter, letter_shift):
   
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
        alph_len = len(alph)

        shift_index = alph.index(letter_shift)

        letter_index = alph.index(letter)

        shifted_index = (letter_index + shift_index) % alph_len

        return alph[shifted_index]

print(shift_by_letter("A", "A"))
print(shift_by_letter("A", "C"))
print(shift_by_letter("B", "K"))
print(shift_by_letter("P", "A"))


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   def vigenere_cipher(message, key):
    key = key * (len(message) // len(key) + 1)  # extend the key to match the length of the message
    key = key[:len(message)]  # truncate the key if it's longer than the message
    result = ''
    for i in range(len(message)):
        if message[i] == ' ':
            result += ' '
        else:
            message_letter_code = ord(message[i]) - 65  # convert letter to number between 0 and 25
            key_letter_code = ord(key[i]) - 65  # convert letter to number between 0 and 25
            shifted_letter_code = (message_letter_code + key_letter_code) % 26  # shift by key amount
            result += chr(shifted_letter_code + 65)  # convert number back to letter
    return result
print(vigenere_cipher("A C", "KEY"))
print(vigenere_cipher("LONGTEXT", "KEY"))
