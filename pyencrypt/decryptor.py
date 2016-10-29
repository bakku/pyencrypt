from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

class Decryptor:

    def __init__(self, in_file_name):
        self.in_file_name = in_file_name

    def decrypt(self):
        self.read_key()
        self.read_file()
        self.extract_parts()
        self.decrypt_text()
        self.try_decode()
        self.write_to_file()

    def read_key(self):
        self.key = SHA256.new(getpass('Key: ').encode('utf-8')).digest()

    def read_file(self):
        self.text_to_decrypt = open(self.in_file_name, 'rb').read()

    def extract_parts(self):
        self.iv = self.text_to_decrypt[:16]
        self.text_to_decrypt = self.text_to_decrypt[16:]

    def decrypt_text(self):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        self.decrypted_text = cipher.decrypt(self.text_to_decrypt)

    def try_decode(self):
        try:
            self.decrypted_text = self.decrypted_text.decode('utf-8')
        except UnicodeDecodeError:
            print('Pyencrypt cannot decrypt. Probably it\'s the wrong key')
            exit(1)

    def write_to_file(self):
        output_file = open(self.in_file_name[:-4], 'w')
        output_file.write(self.decrypted_text)
