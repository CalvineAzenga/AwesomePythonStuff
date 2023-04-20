import string
import random

def generate_password(length: int) -> str:
	characters=string.ascii_letters+string.digits
	password="".join(random.choice(characters) for i in range(length))
	# assert(len(password)==length)

	return password

print(generate_password(15))