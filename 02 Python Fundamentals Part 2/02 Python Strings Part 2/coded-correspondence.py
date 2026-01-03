# Project: Coded Correspondence
# Project Goals
# You and your pen pal, Vishal, have been exchanging letters for some time now. Recently, he has become interested in cryptography and the two of you have started sending encoded messages within your letters.
# In this project, you will use your Python skills to decipher the messages you receive and to encode your own responses! Put your programming skills to the test with these fun cryptography puzzles.


import string

# Caesar Cipher
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
my_msg = "hey there! man"
# Set list with all 26 english alphabet letters
alphabet = list(string.ascii_lowercase)
print(alphabet)

# With an offset of 3 (3 movements)
# h = e
# With an offset of 10 
# h = x
# e = u
# y = 0
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Functions to encrypt and decrypt a letter with Caesar cipher
def caesar_decrypt_letter(letter, offset):
  # Get letter current position
  current_position = alphabet.index(letter)
  # Get new position
  new_position = current_position + offset
  if new_position >= 26:
    new_position = new_position - 26
  new_key = alphabet[new_position]
  return new_key

# Function to encrypt a letter with Caesar cipher
def caesar_encrypt_letter(letter, offset):
  # Get letter current position
  current_position = alphabet.index(letter)
  # Get new position
  new_position = current_position - offset
  if new_position < 0:
    new_position = new_position + 26
  # Get key by value in dictionary by separating the dictionary's values
  # in a list, finding the position of the value with ".index" and getting
  # the key at that position
  new_key = alphabet[new_position]
  return new_key

# Function to decode or encode a message with Caesar cipher
def caesar_decode_encode(message, offset, mode):
  decripted_message = ""

  for letter in message:
    if letter in alphabet:
      if mode == "decrypt":
        decripted_message += caesar_decrypt_letter(letter, offset)
      elif mode == "encrypt":
        decripted_message += caesar_encrypt_letter(letter, offset)
    else:
      decripted_message += letter

  return decripted_message

# Decrypting and encrypting messages with Caesar cipher
print("Decripted message: " + caesar_decode_encode(message, 10, "decrypt"))
print("Sending message: " + caesar_decode_encode(my_msg, 10, "encrypt"))


# Vigenére Cipher
# message: barry is the spy
# keyword phrase: dogdo gd ogd ogd
# Function to create the keyword phrase
def vigenere_create_keyword_phrase(phrase, keyword):
  keyword_phrase = ""
  current_index = 0

  for char in phrase:
    if not char == " ":
      keyword_phrase += keyword[current_index]
      current_index += 1
      if current_index == len(keyword): current_index = 0
    else:
      keyword_phrase += char
  return keyword_phrase

# Function to encode a phrase with Vigenére cipher
def vigenere_encode_phrase(phrase, keyword, alphabet):
  encoded_phrase = ""
  keyword_phrase = vigenere_create_keyword_phrase(phrase, keyword)
  print("keyword_phrase: " + keyword_phrase)

  # Encode each letter
  for index in range(len(phrase)):
    if not keyword_phrase[index] == " ":
      shift_value = alphabet.index(phrase[index]) - alphabet.index(keyword_phrase[index])
      if shift_value < 0:
        shift_value = shift_value + 26
      encoded_phrase += alphabet[shift_value]
    else:
      encoded_phrase += " "
  return encoded_phrase

# Encode a phrase
encoded_phrase = vigenere_encode_phrase("barry is the spy", "dog", alphabet)
print("Enconded phrase: " + encoded_phrase)

# Function to decode a phrase with Vigenére cipher
def vigenere_decode_phrase(phrase, keyword, alphabet):
  print(phrase)
  print(keyword)
  keyword_phrase = vigenere_create_keyword_phrase(phrase, keyword)
  decoded_phrase = ""

  # Decode each letter
  for index in range(len(phrase)):
    if not keyword_phrase[index] == " ":
      shift_value = alphabet.index(phrase[index]) + alphabet.index(keyword_phrase[index])
      if shift_value >= 26:
        shift_value = shift_value - 26
      decoded_phrase += alphabet[shift_value]
    else:
      decoded_phrase += " "

  return decoded_phrase

# Decode the phrase
decoded_phrase = vigenere_decode_phrase(encoded_phrase, "dog", alphabet)
print("Decoded phrase: " + decoded_phrase)
