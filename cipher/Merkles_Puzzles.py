from collections import namedtuple
from random import randint
import string

# Puzzle structure (secret message, index)
Puzzle = namedtuple("Puzzle", ["message", "index"])

# Character set for message and password
charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " "

def create_puzzles(message, num_puzzles, charset=charset):
    """
    Creates a list of puzzles containing the message and random indices.
    """
    puzzles = []
    for i in range(num_puzzles):
        index = randint(0, len(message) - 1)
        puzzles.append(Puzzle(message[index], index))
    return puzzles


def encrypt_message(message, puzzles, charset=charset):
    """
    Encrypts the message using Merkle's Puzzles.
    """
    encrypted_message = "".join([str(puzzle.index) for puzzle in puzzles])
    return encrypted_message


def solve_puzzle(puzzle, charset=charset):
    """
    Solves a puzzle by identifying the message at the specified index.
    """
    message = puzzle.message
    index = puzzle.index
    return message


def decrypt_message(encrypted_message, puzzles, charset=charset):
    """
    Decrypts the message using the solved puzzles.
    """
    message = ""
    for index in encrypted_message:
        for puzzle in puzzles:
            if puzzle.index == int(index):
                message += puzzle.message
                break
    return message


def main():
    # Define the plaintext, password, and number of puzzles
    plaintext = "I am just \"plain\" text ~ 12345."
    password = "P@55w0rd!~ "
    num_puzzles = 10

    # Create and encrypt the message
    puzzles = create_puzzles(plaintext, num_puzzles)
    encrypted_message = encrypt_message(plaintext, puzzles)

    # Solve a random puzzle and verify the message
    random_index = randint(0, len(puzzles) - 1)
    solution = solve_puzzle(puzzles[random_index])
    print(f"Solved puzzle at index {random_index}: {solution}")

    # Decrypt the entire message
    decrypted_message = decrypt_message(encrypted_message, puzzles)
    print(f"Decrypted message: {decrypted_message}")

    # Validate the password
    if decrypted_message == password:
        print("Password is valid!")
    else:
        print("Password is invalid!")


if __name__ == "__main__":
    main()
