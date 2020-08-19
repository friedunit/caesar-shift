# Filename: string_encrypter.py
# Author: John Kaiser
# Date: 8/19/2020
# Purpose: Create 2 functions to encrypt/decrypt a string using an integer shift key based on Caesar Cypher

import string

# create a new list to hold alphabet characters
alpha_array = []

# load alpha_array with lowercase alphabet characters
for ch in string.ascii_lowercase:
    alpha_array.append(ch)

# add in space and underscore
alpha_array.append(' ')
alpha_array.append('_')

# create new list for cypher characters
cypher_array = []


# define encrypting function: name - String to encrypt, shift - integer number to shift
def encrypt_string(name, shift):
    # load up cypher_array starting at shift
    for c in alpha_array[shift:]:
        cypher_array.append(c)
    for c in alpha_array[:shift]:
        cypher_array.append(c)
    # create new dictionary for mapping alpha to cypher
    cypher_dict = {}
    # loop through length of alpha_array
    for i in range(len(alpha_array)):
        # load cypher dictionary to map alpha_array to cypher_array
        cypher_dict[alpha_array[i]] = cypher_array[i]
    name = name.lower()
    encrypted = ""
    # now append characters from name to cypher equivalent to encrypted String
    for i in range(len(name)):
        encrypted += (cypher_dict[name[i]])

    return encrypted


# decrypt_string function to reverse the encrypted string. Must have the same shift integer
def decrypt_string(name, shift):
    # clear the cypher array to start over
    cypher_array.clear()
    for c in alpha_array[shift:]:
        cypher_array.append(c)
    for c in alpha_array[:shift]:
        cypher_array.append(c)
    cypher_dict = {}
    for i in range(len(alpha_array)):
        cypher_dict[cypher_array[i]] = alpha_array[i]
    name = name.lower()
    decrypted = ""
    for i in range(len(name)):
        decrypted += (cypher_dict[name[i]])

    return decrypted


print(encrypt_string('String to encrypt', 6))
