#This program will encrypt, or decrypt, a text to share hidden messages.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
loop_on = True
while loop_on:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    def caesar(t, s, cipher_direction):
        cipher_text = ""
        for letter in t:
            if letter not in alphabet:
                cipher_text += letter
            else:
                pos_in_alphabet = alphabet.index(letter)
                if s > 25 and cipher_direction == "encode":
                    cipher_text += alphabet[pos_in_alphabet + (s % 26)]
                elif s > 25 and cipher_direction == "decode":
                    cipher_text += alphabet[pos_in_alphabet - (s % 26)]
                elif cipher_direction == "encode":
                    cipher_text += alphabet[pos_in_alphabet + s]
                elif cipher_direction == "decode":
                    cipher_text += alphabet[pos_in_alphabet - s]
        print("".join(cipher_text))
    caesar(t=text, s=shift, cipher_direction=direction)
    restart = input("Do you want to go again?\n")
    if restart == "no".lower() or restart == "n".lower():
        print("Goodbye")
        loop_on = False