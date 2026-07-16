"""
Instructions:
Caesar Cipher 1:
You are going to build an encryption and decryption program using the Caesar cipher (https://en.wikipedia.org/wiki/Caesar_cipher).

TODO-1
Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2
Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.

You can use the built-in Python index() function to find out the position of an item in a list. e.g.

fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
e.g. If we have following values:

plain_text = "hello"
shift_amount = 1
The final encrypted output should be:

Here is the encoded result: ifmmp

Where each of the letters of 'hello' is shifted up by 1.

TODO-3
Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.

TODO-4:
What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

Caesar Cipher 2:
TODO-1:
Create a function called decrypt() that takes original_text and shift_amount as 2 inputs.

TODO-2:
Inside the decrypt() function, shift each letter of the original_text forwards in the alphabet backwards by the shift_amount and print the decrypted text.

TODO-3:
- Combine the encrypt() and decrypt() functions into a single function called caesar().
- Use the value of the user chosen direction variable to determine which functionality to use.
- call the caesar function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

Caesar Cipher 3:
TODO-1
Import and print the logo from art.py when the program starts.

TODO-2
What happens if the user enters a number/symbol/space that's not in the List alphabet?

Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?

e.g.

original_text = "meet me at 3!"
cipher_text = "XXXX XX XX 3!"

TODO-3:
Can you figure out a way to restart the cipher program?

e.g.

Type 'yes' if you want to go again. Otherwise, type 'no'.

If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again.
"""
"""
Demo from AppBrewery:
https://appbrewery.github.io/python-day8-demo/
"""

from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
#         cipher_text += alphabet[shifted_position]

# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = (alphabet.index(letter) - shift_amount) %len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {cipher_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

while repeat:
    # encrypt(original_text=text, shift_amount=shift)
    caesar(text, shift, direction)
    while True:
        repeat_prompt = input("Type 'yes' to encrypt or decrypt another message, or type 'no' to exit the program.").strip().lower()
        if repeat_prompt in("yes", "y"):
            break
        elif repeat_prompt in("no", "n"):
            repeat = False
            break
        else:
            print("Invalid input. Please try again.")

