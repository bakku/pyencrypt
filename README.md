# Encrypt/Decrypt files using pyencrypt

This is a small python script which can be used to encrypt/decrypt files

## Installation

    pip install pyencrypt


## Usage

### Encryption

    pyencrypt -e random_file.txt

The encryption mode encrypts the file using the given key and creates an encrypted file using the same filename with `.pec` added to the end. In the above example the filename would be therefore `random_file.txt.pec`.

### Decryption

    pyencrypt -d random_file.txt.pec

The decryption mode decrypts the file and writes creates a decrypted file using the original filename

### Security

Pyencrypt uses the AES 256 bit algorithm which is regarded as safe today. Note that pyencrypt does not use any authentication method so it is not safe against modifications.

If the key was forgotten there is no possible way to reconstruct the key either than breaking the AES encryption using brute force mechanisms or other possible ways to break encryptions.
