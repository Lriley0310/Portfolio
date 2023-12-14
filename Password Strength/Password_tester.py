import math

def main():
    password = input("Please enter the password: ")  # Move assignment of password inside the function
    num_combinations_password = num_combinations_password(password)
    bit_strength = bit_strength(password)
    print(f"There are {num_combinations_password:,} combinations.")
    print(f"That is equivalent to a key of {bit_strength:.2f} bits.")


def count_alphabet_size(password):

    lowercase_letters = set('abcdefghijklmnopqrstuvwxyz')

    uppercase_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    digits = set('0123456789')

    symbols = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ')

    alphabet_size = 0

    seen_categories = set()

    for char in password:

        if char in lowercase_letters and 'lowercase' not in seen_categories:

            alphabet_size += 26

            seen_categories.add('lowercase')

        elif char in uppercase_letters and 'uppercase' not in seen_categories:

            alphabet_size += 26

            seen_categories.add('uppercase')

        elif char in digits and 'digits' not in seen_categories:

            alphabet_size += 10

            seen_categories.add('digits')

        elif char in symbols and 'symbols' not in seen_categories:

            alphabet_size += 33

            seen_categories.add('symbols')

    # print(alphabet_size)

    return alphabet_size

def num_combinations_password(password):

    alphabet_size = count_alphabet_size(password)

    password_length = len(password)

    # print(alphabet_size), print(password_length)

    possible_combinations = alphabet_size ** password_length

    return possible_combinations

def bit_strength(password):

    num_combinations = num_combinations_password(password)

    bit_strength = math.log2(num_combinations)

    return math.ceil(bit_strength - 1)

def main():
    password = input("Please enter the password: ")  # Move assignment of password inside the function
    num_combinations_password_final = num_combinations_password(password)
    bit_strength_final = bit_strength(password)
    print(f"There are {num_combinations_password_final:,} combinations.")
    print(f"That is equivalent to a key of {bit_strength_final:.2f} bits.")

if __name__ == "__main__":
    main()

    

