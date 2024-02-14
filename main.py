alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    result = ''
    for letter in text:
        letter_index = alphabet.index(letter)
        new_letter_index = (letter_index + shift) % (len(alphabet) - 1)
        result += alphabet[new_letter_index]
    print(result)

def decrypt(text, shift):
    result = ""
    for letter in text:
        cyphered_letter_index = alphabet.index(letter)
        new_letter_index = cyphered_letter_index - shift
        result += alphabet[new_letter_index]
    print(result)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("wrong input")