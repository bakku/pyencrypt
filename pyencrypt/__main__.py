import sys

from pyencrypt.cli import PyencryptCLI 
from pyencrypt.encryptor import Encryptor
from pyencrypt.decryptor import Decryptor

def main():
    cli = PyencryptCLI(sys.argv)
    cli.parse()

    if cli.encrypt:
        encryptor = Encryptor(cli.in_file)
        encryptor.encrypt()
    else:
        decryptor = Decryptor(cli.in_file)
        decryptor.decrypt()

if __name__ == '__main__':
    main()
