#              | Caesar Cipher encryption freeCodeCamp exercise |
#
# --------------------------------------------------------------------------------
# Overview:
#
# Caesar cipher is one of the simplest techniques to encrypt text.
# It consists of substituting each letter of the plain text with the
# letter found at a fixed number of positions down the alphabet.
#
# Example (shift = 5):
# a -> f, b -> g, c -> h, etc.
#
# --------------------------------------------------------------------------------
#
# Concepts learned in this exercise:
#
# 1. str.maketrans()
#    Creates a translation table by mapping characters from one string to another
#    of equal length. Internally, characters are stored as Unicode ordinal values.
#
# 2. translate()
#    Uses a translation table to replace characters in a string.
#
# ---------------------------------------------------------------------------------
# Decryption:
#
# The same way the encryption process occurs, decryption takes place by the reverse
# operation. In the decrypt function, the encrypt=False parameter is passed to the
# caesar function. This triggers the if not encrypt condition and sets shift to a
# negative value, reversing the direction of the translation table for decryption.
#
# ---------------------------------------------------------------------------------
# Caesar cipher is weak due to only 25 shift possibilities.
#
# Example:
# 1. abcdefghijklmnopqrstuvwxyz
# 2. bcdefghijklmnopqrstuvwxyza
# 3. cdefghijklmnopqrstuvwxyzab
# 4. defghijklmnopqrstuvwxyzabc
# 5. efghijklmnopqrstuvwxyzabcd
#
# And so on...
#
# Here is the Caesar Cipher example built in freeCodeCamp below:
# ---------------------------------------------------------------


def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = ('Pbatengf lbh penpxrq gur pbqr!')
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

# Output:
# Congrats you cracked the code!
