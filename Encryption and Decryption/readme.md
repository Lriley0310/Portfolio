# File Encryption and Decryption Application

## Overview
This application allows you to securely encrypt and decrypt files using the Advanced Encryption Standard (AES) with the `cryptography` library. It provides a simple Command-Line Interface (CLI) to generate encryption keys, encrypt files, and decrypt files. After encryption, the original file is deleted to ensure data security.

## Features
- **Key Generation**: Generate a secure encryption key and save it to a specified file.
- **File Encryption**: Encrypt the contents of a file using a generated key and save the encrypted content to a new file. The original file is deleted after encryption.
- **File Decryption**: Decrypt an encrypted file using the specified key and save the decrypted content to a new file.

## Requirements
- Python 3.6 or higher
- `cryptography` library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Lriley0310/Portfolio.git
   cd Encryption%20and%20Decryption
2. Install the required dependencies:
    pip isntall cryptography

## Usage
1. Generate Key:<br>
    To generate a secure key and save it to a specified file:<br>  
        python main.py generate_key --key keyfile.key

2. Encrypt File:<br>
    To Encrypt a specified file using the generated key (the original message will be deleted after encryption!):<br>  
        python main.py encrypt --file [file name] --key keyfile.key
    
3. Decrypt Files:<br>
    To decrypt the file that you previously encrypted:<br>  
        python main.py decrypt --file [file name].enc --key keyfile.key