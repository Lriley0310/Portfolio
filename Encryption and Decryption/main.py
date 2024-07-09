# File: file_crypto.py
from cryptography.fernet import Fernet
import argparse
import os

# Generate a key and save it to a file
def generate_key(key_path):
    try:
        key = Fernet.generate_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        print(f"Key generated and saved to {key_path}")
    except Exception as e:
        print(f"Error generating key: {e}")

# Load the key from a file
def load_key(key_path):
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
        print(f"Key loaded from {key_path}")
        return key
    except Exception as e:
        print(f"Error loading key: {e}")
        return None

# Encrypt a file and delete the original
def encrypt_file(file_path, key_path):
    try:
        key = load_key(key_path)
        if key is None:
            print("Failed to load key.")
            return

        fernet = Fernet(key)

        with open(file_path, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
        
        encrypted_file_path = file_path + '.enc'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        os.remove(file_path)
        print(f"File encrypted and saved to {encrypted_file_path}. Original file {file_path} has been deleted.")
    except Exception as e:
        print(f"Error encrypting file: {e}")

# Decrypt a file
def decrypt_file(file_path, key_path):
    try:
        key = load_key(key_path)
        if key is None:
            print("Failed to load key.")
            return

        fernet = Fernet(key)

        with open(file_path, 'rb') as enc_file:
            encrypted = enc_file.read()
        
        decrypted = fernet.decrypt(encrypted)
        
        decrypted_file_path = file_path.rstrip('.enc')
        with open(decrypted_file_path, 'wb') as dec_file:
            dec_file.write(decrypted)

        print(f"File decrypted and saved to {decrypted_file_path}")
    except Exception as e:
        print(f"Error decrypting file: {e}")

# Main function for CLI
def main():
    parser = argparse.ArgumentParser(description="Encrypt and Decrypt files")
    parser.add_argument('action', choices=['generate_key', 'encrypt', 'decrypt'], help="Action to perform")
    parser.add_argument('--file', type=str, help="File path for encryption/decryption")
    parser.add_argument('--key', type=str, help="Key file path")

    args = parser.parse_args()

    if args.action == 'generate_key':
        if args.key:
            generate_key(args.key)
        else:
            print("Please provide --key argument to specify where to save the key.")
    elif args.action == 'encrypt':
        if args.file and args.key:
            if os.path.isfile(args.file):
                encrypt_file(args.file, args.key)
            else:
                print(f"The file {args.file} does not exist.")
        else:
            print("Please provide --file and --key arguments for encryption.")
    elif args.action == 'decrypt':
        if args.file and args.key:
            if os.path.isfile(args.file):
                decrypt_file(args.file, args.key)
            else:
                print(f"The file {args.file} does not exist.")
        else:
            print("Please provide --file and --key arguments for decryption.")

if __name__ == "__main__":
    main()
