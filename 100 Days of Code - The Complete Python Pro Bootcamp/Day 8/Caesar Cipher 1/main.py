alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs



def encrypt(original_text, shift_amount):
    encrypted_text = ''

    for letter in original_text:
        new_position = alphabet.index(letter) + shift_amount
        new_position %= len(alphabet)
        encrypted_text += alphabet[new_position]

    print(encrypted_text)

encrypt("hello", 1)


# encrypted_word =[]
# def encrypt(original_text, shift_amount):
#     listed_word =  list(original_text)
#     indexes_of_word = []
#     for letter in listed_word:
#         indexes_of_word.append(int(alphabet.index(letter)) + shift_amount)
#
#     for index in indexes_of_word:
#         encrypted_word.append(alphabet[index])
#
#     print(indexes_of_word)
#     print(''.join(encrypted_word))




# final_word = []
# indexes = [7,4,11,11,14]
# new_indexes = []
# for kek in indexes:
#     kek += 1
#     new_indexes.append(kek)
#     final_word.append(alphabet[kek])




# encrypt('hello', 1)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

