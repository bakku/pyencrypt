import sys, os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from pyencrypt.cli import PyencryptCLI 

cli = PyencryptCLI(sys.argv)
print(cli.arguments)
