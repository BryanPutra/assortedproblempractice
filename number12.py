import string
def caesar_cipher(str):
    alphabet = string.ascii_lowercase
    new_word = ""
    for x in str:
        next = alphabet.find(x) + 13
        if next > 25:
            next = next - 26
            new_letter = alphabet[next]
            new_word = new_word + new_letter
