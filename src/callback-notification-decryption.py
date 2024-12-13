
from Crypto.Cipher import AES  # Import the AES encryption algorithm from the Crypto library
from base64 import b64decode
import binascii  # For hexadecimal and binary conversion
import requests  # Used to send HTTP requests
import json  # For JSON encoding and decoding
from Crypto.Util.Padding import unpad
  

# VGGPay sends callback data to your server. Here is an example of how to decrypt the callback data.

def hex2bin(hex_str):
    return binascii.unhexlify(hex_str)  # Decode a hex string into a byte array using the binascii library



# Decryption function
def decrypt_data(encrypted_data, secret_key, secret_iv):
    key = binascii.unhexlify(secret_key)
    iv = binascii.unhexlify(secret_iv)

    encrypted = b64decode(encrypted_data)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted), AES.block_size)

    return decrypted_data.decode('utf-8')


# VGGPay sends callback data to your server. Here is an example of how to decrypt the callback data.

secret_key = "88d4012da55e249ab48cffbe2f19d6326e524680d5dfa8b5990b02fdc9473682"
secret_iv = "6ad4dabbb9844769fb33e8655a78a7fc"
encrypted_data = "jdtdW1+nP8D3geSHQ0+5h0V5Dpez3Lmon0dpW6Dd4BnOEPDqdWNeuow7MM0XHxshHDJxP1QXslO81Enw+JryoRqEWCQYaS282TjqxXtxXfkL1NeLqwlJsKk/EKCnlDGZy2tP5fgCrGaWxAhGWVUtrTppidgFmJrHGh1c5qKFZe0jsxzIY+YI37KyhsOCJzKYgP4GwkQljh+SNF0AuH6vmnI710cczfIXjT2/GJjnJugnVtYuV/W4UN8qgPj3NAZWuDXM6oe1xTufGb8lNU1HctbBRheqUU2/xyGqJz8AOZnb9Z6//r7U90vfdhBolZ94PojBucyifPyShnTaNS+Uy4ZB6UmACWmFtDZTjmOzLbm/dL0ppFVxqMbxQjpTr7OeZKHEkMZLoxJygjThoTbUNQspM5DeVgwgeXHBUnlGma9MkOuIPppfbWrGbtlpZVj6"


# Call the decryption function
decrypted_data = decrypt_data(encrypted_data, secret_key, secret_iv)

print(decrypted_data)

 





 



