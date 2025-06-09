from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


class AsymmetricEncryption:
    """ Класс для асимметричного шифрования с использованием алгоритма RSA """

    @staticmethod
    def generate_rsa_keys() -> tuple[RSAPrivateKey, RSAPublicKey]:
        """
        Генерирует пару RSA ключей
        :return: кортеж из приватного и публичного ключей
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return private_key, private_key.public_key()

    @staticmethod
    def serialization_asymmetric_public_key(public_key: RSAPublicKey) -> bytes:
        """
        Сериализует публичный RSA ключ в PEM формат
        :param public_key: публичный ключ
        :return: публичный ключ в PEM формате
        """
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem_public_key

    @staticmethod
    def serialization_asymmetric_private_key(private_key: RSAPrivateKey) -> bytes:
        """
        Сериализует приватный RSA ключ в PEM формат
        :param private_key: приватный ключ
        :return: приватный ключ в PEM формате
        """
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        return pem_private_key

    @staticmethod
    def rsa_encrypt(public_key: RSAPublicKey, data: bytes) -> bytes:
        """
        Шифрует данные
        :param public_key: публичный ключ
        :param data: данные
        :return: зашифрованные данные
        """
        return public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def rsa_decrypt(private_key: RSAPrivateKey, encrypted_data: bytes) -> bytes:
        """
        Расшифровывает данные
        :param private_key: приватный ключ
        :param encrypted_data: зашифрованные данные
        :return: расшифрованные данные
        """
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )