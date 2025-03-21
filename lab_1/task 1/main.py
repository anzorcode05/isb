import argparse

import sys

from argparse import ArgumentParser, Namespace

from cipher import encrypt_message


def parse_arg() -> Namespace:
    """
    Parser for command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Tool for encrypting text using the Vigenère cipher.")
    parser.add_argument('input_text', type=str, help='Name of input text file')
    parser.add_argument('output_text', type=str, help='Name of output text file')
    parser.add_argument('key_filename', type=str, help='Filename containing the key')
    return parser.parse_args()


def load_file_content(file_path: str) -> str:
    """
    Reads the content of a file.

    :param file_path: Path to the file to be read.
    :return: The content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)


def save_to_file(file_path: str, content: str) -> None:
    """
    Writes content to a file.

    :param file_path: Path to the file where the content will be saved.
    :param content: The content to write to the file.
    :return: None.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")
        sys.exit(1)


def run_program() -> None:
    """
    Main function to execute the encryption process.
    """

    arguments = parse_arg()


    encryption_key = load_file_content(arguments.key_filename)
    text_to_encrypt = load_file_content(arguments.input_text)


    encrypted_content = encrypt_message(text_to_encrypt, encryption_key)


    save_to_file(arguments.output_text, encrypted_content)


if __name__ == "__main__":
    run_program()