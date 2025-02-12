import base64

        
encoded_string = "iaPkqst7ig3Q7HQdnxYcYgUGyKsQXxFKckx6"
# Add padding if necessary
padding = len(encoded_string) % 4
if padding:
    encoded_string += '=' * (4 - padding)

decoded_bytes = base64.b64decode(encoded_string)
print("Decoded bytes:", decoded_bytes)
print("First few bytes:", decoded_bytes[:10])
ascii_text = "".join(chr(b) for b in decoded_bytes if 32 <= b <= 126)
print("ASCII text in decoded bytes:", ascii_text)