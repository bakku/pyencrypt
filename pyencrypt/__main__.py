import sys

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from pyencrypt.cli import PyencryptCLI 
from pyencrypt.encryptor import Encryptor

cli = PyencryptCLI(sys.argv)
cli.parse()

if cli.encrypt:
    encryptor = Encryptor(cli.in_file, cli.out_file)
    encryptor.encrypt()
else:
    print("hi")
