def caesar_cipher_encrypt(str_to_encrypt, n):
    """
    Encrypt string using Caesar cipher by n positions
    
    This function builds one of the most widely known encryption 
    techniques, _Caesar's cipher_. This works as follows: 
    you should be given a string str_to_encrypt and an encoding 
    integer n, which then be used to replace each initial letter 
    to the encrypted one by simply shifting the letter by n positions.
    
    Parameters:
        str_to_encrypt: string
        n: shift parameter
        
    Returns:
        n-encrypted string
    
    Examples:
    >>> caesar_cipher_encrypt('a', 1)
    'b'
    >>> caesar_cipher_encrypt('abc', 1)
    'bcd'
    >>> caesar_cipher_encrypt('abc', 4)
    'efg'
    >>> caesar_cipher_encrypt('thisistherealdeal', 6)
    'znoyoyznkxkgrjkgr'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in str_to_encrypt:
        if char in alphabet:
            original_pos = alphabet.index(char) # finds the position (0-25) of char in the alphabet
            new_pos = (original_pos + n) % 26 # if the shift goes beyond 'z', it loops back to 'a'
            encrypted.append(alphabet[new_pos])
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)
    

def caesar_cipher_decrypt(str_to_decrypt, n):
    """
    Decrypt Caesar cipher by n positions
    
        
    Parameters:
        str_to_decrypt: string
        n: shift parameter
        
    Returns:
        n-decrypted string
    
    Examples:
    >>> caesar_cipher_decrypt('b', 1)
    'a'
    >>> caesar_cipher_decrypt('bcd', 1)
    'abc'
    >>> caesar_cipher_decrypt('efg', 4)
    'abc'
    >>> caesar_cipher_decrypt('znoyoyznkxkgrjkgr', 6)
    'thisistherealdeal'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = []
    for char in str_to_decrypt:
        if char in alphabet:
            encrypted_pos = alphabet.index(char)
            decrypted_pos = (encrypted_pos - n) % 26
            decrypted.append(alphabet[decrypted_pos])
        else:
            decrypted.append(char)
    return ''.join(decrypted)

    


