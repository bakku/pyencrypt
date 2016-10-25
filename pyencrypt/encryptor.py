from getpass import getpass

class Encryptor:

    def __init__(self, in_file_name, out_file_name):
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name

    def encrypt(self):
        self.read_key()
        print(self.key)

    def read_key(self):
        self.key = getpass('Key: ')

