from sys import getsizeof
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

class Encryptor:

    def __init__(self, in_file_name):
        self.in_file_name = in_file_name

    def encrypt(self):
        self.read_key()
        self.read_file()
        self.encrypt_text()
        self.write_encrypted_text_to_file()

    def read_key(self):
        self.key = SHA256.new(getpass('Key: ').encode('utf-8')).digest()

    def read_file(self):
        self.text_to_encrypt = bytes(open(self.in_file_name).read().encode('utf-8'))

    def encrypt_text(self):
        random_iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, random_iv)

        padding_length = AES.block_size - (len(self.text_to_encrypt) % AES.block_size)
        self.text_to_encrypt += bytes([padding_length]) * padding_length

        self.text_to_encrypt = random_iv + self.text_to_encrypt
        
        self.encrypted_text = cipher.encrypt(self.text_to_encrypt) 

    def write_encrypted_text_to_file(self):
        output_file = open(self.in_file_name + '.pec', 'wb')
        output_file.write(self.encrypted_text)
