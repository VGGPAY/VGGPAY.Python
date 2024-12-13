
from Crypto.Cipher import AES  # Import the AES encryption algorithm from the Crypto library
from Crypto.Util.Padding import pad  # Import PKCS#7 padding from the Crypto library
import base64  # For Base64 encoding and decoding
import binascii  # For hexadecimal and binary conversion
import requests  # Used to send HTTP requests
import json  # For JSON encoding and decoding

# Convert hex string to byte array
def hex2bin(hex_str):
    return binascii.unhexlify(hex_str)  # Decode a hex string into a byte array using the binascii library

# Encrypting data
def encrypt_data(plaintext, key_hex, iv_hex):
    key = hex2bin(key_hex)  # Convert hex key to byte array
    iv = hex2bin(iv_hex)    # Convert hexadecimal IV to byte array

    # Creating an Encryptor Using AES-CBC Mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Apply PKCS#7 padding to data
    padded_data = pad(plaintext.encode(), AES.block_size)
    # Encrypted padded data
    encrypted = cipher.encrypt(padded_data)

    # Encode the encrypted data in Base64 and return it
    return base64.b64encode(encrypted).decode()






# Sample Data
project_id = '999DEMO'  # Project ID
secret_key = '88d4012da55e249ab48cffbe2f19d6326e524680d5dfa8b5990b02fdc9473682'  # Hexadecimal key
secret_iv = '6ad4dabbb9844769fb33e8655a78a7fc'  # Hexadecimal IV

# Order data
data = {
    "projectid": project_id,                  # Project ID
    "m_orderid": "yourShopOrder12345679",    #  Your mall order number
    "currency": "EUR",                       # Currency Type
    "amount": "815.23",                      # Order amount
    "firewall": "2",                         # Firewall settings
    "notify_url": "https://my-notify-api.com", # Notification callback URL
    "notify_txt": '{"Product":"iPhone 13","modelColor":"red","myStrings":"Custom Strings"}'  # Customize notification content
}




# Convert order data to a JSON string
json_data = json.dumps(data)

# Encrypting JSON data
encrypted_data = encrypt_data(json_data, secret_key, secret_iv)

# Encapsulate the encrypted data and project ID into a JSON string
post_data = json.dumps({
    "data": encrypted_data,  # Encrypted data
    "projectid": project_id  # Project ID
})

# The URL of the target API
url = "https://sapi.vggpay.com/api/v2/createorder"

try:
    # Sending HTTP POST Request
    response = requests.post(
        url,
        data=post_data,
        headers={'Content-Type': 'application/json'},
        verify=False
    )
    # Response Status
    print("Response Status:", response.status_code)
    # Response Body
    print("Response Body:", response.text)

except requests.RequestException as e:
    print("Request failed:", e)




