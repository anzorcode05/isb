from const import ALPHABET

# Словарь для быстрого поиска индексов символов
ALPHABET_INDEX = {char: idx for idx, char in enumerate(ALPHABET)}


def extend_key(_key: str, target_length: int) -> str:
    """
    Returns a key character for a given position by using modulo operation.

    :param _key: The original key.
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


def decrypt_char(encrypted_char: str, key_char: str) -> str:
    """
    Decrypts a single character using the Vigenère cipher.

    :param encrypted_char: The character to be decrypted.
    :param key_char: The corresponding key character.
    :return: The decrypted character.
    """
    if encrypted_char.isalpha():

        encrypted_lower = encrypted_char.lower()
        key_lower = key_char.lower()


        try:
            encrypted_index = ALPHABET_INDEX[encrypted_lower]
            key_index = ALPHABET_INDEX[key_lower]
        except KeyError:
            raise ValueError(f"Character '{encrypted_char}' or '{key_char}' not found in alphabet.")


        decrypted_index = (encrypted_index - key_index) % len(ALPHABET)


        decrypted_char = ALPHABET[decrypted_index]
        return decrypted_char.upper() if encrypted_char.isupper() else decrypted_char

    else:
        # Если символ не буква, возвращаем его без изменений
        return encrypted_char


def encrypt_message(message: str, secret_key: str) -> str:
    """
    Encrypts a message using the Vigenère cipher.

    :param message: The message to be encrypted.
    :param secret_key: The encryption key.
    :return: The encrypted message.
    """
    if not message:
        raise ValueError("Message cannot be empty")

    if not secret_key:
        raise ValueError("Secret key cannot be empty")

    encrypted_message = ""

    for i in range(len(message)):
        message_char = message[i]
        key_char = secret_key[i % len(secret_key)]  # Используем остаток от деления
        encrypted_message += encrypt_char(message_char, key_char)

    return encrypted_message


def decrypt_message(encrypted_message: str, secret_key: str) -> str:
    """
    Decrypts a message using the Vigenère cipher.

    :param encrypted_message: The message to be decrypted.
    :param secret_key: The decryption key.
    :return: The decrypted message.
    """
    if not encrypted_message:
        raise ValueError("Encrypted message cannot be empty")

    if not secret_key:
        raise ValueError("Secret key cannot be empty")

    decrypted_message = ""

    for i in range(len(encrypted_message)):
        encrypted_char = encrypted_message[i]
        key_char = secret_key[i % len(secret_key)]  # Используем остаток от деления
        decrypted_message += decrypt_char(encrypted_char, key_char)

    return decrypted_message