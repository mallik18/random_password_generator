#: 1.Generating random passwrods with user given lenght
import string
import secrets

class Gen_Password:
	def __init__(self, lenght):
		self.lenght = lenght
		self.rand_passw = None

	def generate_random_pass(self):
		chars = string.ascii_letters + string.digits + string.punctuation
		self.rand_passw = ''.join(secrets.choice(chars) for i in range(self.lenght))

	def get_generated_password(self):
		print("Random Password generated =", self.rand_passw)

def main():
	lenght = int(input("Enter the lenght of the password to be generated ="))
	if lenght > 0:
		passw = Gen_Password(lenght)
		passw.generate_random_pass()
		passw.get_generated_password()
	else:
		print("Try Again.. Enter password lenght greater than 0")


if __name__ == "__main__":
	main()
