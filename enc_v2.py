from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
with open("pass.key", "wb") as key_file: key_file.write(key)
code = input("ENC: ").encode()
a = Fernet(key)
code = a.encrypt(code)
print(code)