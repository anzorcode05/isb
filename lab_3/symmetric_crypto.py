import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricalEncryption:
    """ Класс для симметричного шифрования с использованием алгоритма AES """

    @staticmethod
    def generate_key(key_size: int) -> bytes:
        """
        Генерирует ключ
        :param key_size: размер ключа в битах
        :return: ключ
        """
        return os.urandom(key_size // 8)

    @staticmethod
    def padding_data(data: bytes) -> bytes:
        """
        Добавляет паддинг к данным
        :param data: данные
        :return: данные с добавленным паддингом
        """
        padder = padding.ANSIX923(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    @staticmethod
    def encrypt_data(data: bytes, key: bytes) -> bytes:
        """
        Шифрует данные
        :param data: данные
        :param key: ключ
        :return: зашифрованные данные
        """
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(SymmetricalEncryption.padding_data(data)) + encryptor.finalize()

        return iv + ciphertext

    @staticmethod
    def unpadding_data(data: bytes) -> bytes:
        """
        Удаляет паддинг из данных
        :param data: данные
        :return: данные без паддинга
        """
        unpadder = padding.ANSIX923(128).unpadder()
        unpadded_data = unpadder.update(data) + unpadder.finalize()
        return unpadded_data

    @staticmethod
    def decrypt_data(data: bytes, key: bytes) -> bytes:
        """
        Расшифровывает данные
        :param data: данные
        :param key: ключ
        :return: расшифрованные данные
        """
        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        return SymmetricalEncryption.unpadding_data(padded_data)
