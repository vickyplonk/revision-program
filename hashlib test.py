import hashlib
phrase=input("enter something: ")
phrase=phrase.encode()

print(hashlib.sha256(phrase).hexdigest())
