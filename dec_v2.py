from cryptography.fernet import Fernet

s = input("DEC: ")

code = bytes(s, "utf-8")
def call_key(): return open("pass.key", "rb").read()
key = call_key()
b = Fernet(key)
decoded_code = b.decrypt(code)
print(decoded_code)


