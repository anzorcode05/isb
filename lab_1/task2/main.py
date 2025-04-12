import sys

from constant import *
from decryptor import *


def write_encrypted_text(filename: str, text: str) -> None:
    """
    Function to write text to file.

    :param filename: Path to the file where the text will be saved.
    :param text: Encrypted text
    :return: None
    """

    try:

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:

        print(f"Error writing to file '{filename}': {e}")
        sys.exit(1)


def read_file(filename: str) -> str:
    """
    Text reading function.

    :param filename: Path to the text to be read
    :return: The input text
    """

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except:

        print(f"File '{filename}' not found.")
        sys.exit(1)


def main():

    save_freq_to_json(RUS_FREQ_JSON, RUSSIAN_FREQ)

    encrypted_text = read_file(ENCRYPTED_TEXT_TXT)

    text_freq = calculate_freq(encrypted_text)

    save_freq_to_json(ENCRYPTED_FREQ_JSON, text_freq)

    rus_dict = load_freq_from_json(RUS_FREQ_JSON)
    encrypt_dict = load_freq_from_json(ENCRYPTED_FREQ_JSON)

    encrypt_rus_dict = create_encrypt_rus_dict(encrypt_dict, rus_dict)


    key = load_freq_from_json(KEY_JSON)

    decrypted_text = decrypt_text(encrypted_text, key)

    write_encrypted_text(DECRYPTED_TEXT_TXT, decrypted_text)


if __name__ == '__main__':
    main()