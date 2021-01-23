import string

def caesar(text, shift, alphabets):
    def shifted_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabets = tuple(map(shifted_alphabet, alphabets))
    final_alphabets = ''.join(alphabets)
    final_shifted_alphabets= "".join(shifted_alphabets)
    table= str.maketrans(final_alphabets,final_shifted_alphabets)
    return text.translate(table)

plain_text = input("Enter the text to be encrypted: ")
digit = int(input("Enter the shift value: "))

print(caesar(plain_text,digit,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))