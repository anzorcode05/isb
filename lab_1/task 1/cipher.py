from const import ALPHABET

#словарь для быстрого поиска индексов символов
ALPHABET_INDEX = {char: idx for idx, char in enumerate(ALPHABET)}

def extend_key(_key: str, target_length: int) -> str:
    """
    Returns a key character for a given position by using modulo operation.

    :param _key: The original  key.
    :param target_length: The desired length of the extended key.
    :return: The key character for the given position.
    """
    if not _key:
        raise ValueError("Secret key cannot be empty!")


    return _key[target_length % len(_key)]


def encrypt_char(original_char: str, key_char: str) -> str:
    """
    Encrypts a single character using the Vigenère cipher.

    :param original_char: The character to be encrypted.
    :param key_char: The corresponding key character.
    :return: The encrypted character.
    """
    if original_char.isalpha():

        original_lower = original_char.lower()
        key_lower = key_char.lower()


        try:
            original_index = ALPHABET_INDEX[original_lower]
            key_index = ALPHABET_INDEX[key_lower]
        except KeyError:
            raise ValueError(f"Character '{original_char}' or '{key_char}' not found in alphabet.")


        encrypted_index = (original_index + key_index) % len(ALPHABET)


        encrypted_char = ALPHABET[encrypted_index]
        return encrypted_char.upper() if original_char.isupper() else encrypted_char

    else:

        return original_char