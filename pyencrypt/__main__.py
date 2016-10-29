import sys

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from pyencrypt.cli import PyencryptCLI 
from pyencrypt.encryptor import Encryptor
from pyencrypt.decryptor import Decryptor

cli = PyencryptCLI(sys.argv)
cli.parse()

if cli.encrypt:
    encryptor = Encryptor(cli.in_file)
    encryptor.encrypt()
else:
    decryptor = Decryptor(cli.in_file)
    decryptor.decrypt()
