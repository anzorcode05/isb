import argparse

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from asymmetric_cripto import AsymmetricEncryption
from symmetric_crypto import SymmetricalEncryption
from work_with_files import read_binary_file, write_binary_file, read_json, write_json


def generate_keys(key_size, public_key_path: str,
                  private_key_path: str,
                  encrypted_symmetric_key_path: str ) -> None:
    """
    Генерирует все ключи
    :param key_size: размер симметричного ключа
    :param public_key_path: путь для сохранения публичного RSA ключа
    :param private_key_path: путь для сохранения приватного RSA ключа
    :param encrypted_symmetric_key_path: путь для сохранения зашифрованного симметричного ключа
    """
    try:
        symmetric_key = SymmetricalEncryption.generate_key(key_size)
        private_key, public_key = AsymmetricEncryption.generate_rsa_keys()

        serialized_public = AsymmetricEncryption.serialization_asymmetric_public_key(public_key)
        serialized_private = AsymmetricEncryption.serialization_asymmetric_private_key(private_key)

        encrypted_symmetric_key = AsymmetricEncryption.rsa_encrypt(public_key, symmetric_key)

        write_binary_file(public_key_path, serialized_public)
        write_binary_file(private_key_path, serialized_private)
        write_binary_file(encrypted_symmetric_key_path, encrypted_symmetric_key)

    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе генерации ключей: {str(e)}")


def encrypt_data(original_text_path: str,
                 private_key_path: str,
                 encrypted_symmetric_key_path: str,
                 encrypt_text_path: str) -> None:
    """
    Шифрует данные
    :param original_text_path: путь к файлу с исходными данными для шифрования
    :param private_key_path: путь к файлу с приватным RSA ключом
    :param encrypted_symmetric_key_path: путь к файлу с зашифрованным симметричным ключом
    :param encrypt_text_path: путь для сохранения зашифрованных данных
    """
    try:
        original_text = read_binary_file(original_text_path)
        private_key_bytes = read_binary_file(private_key_path)
        encrypted_symmetric_key = read_binary_file(encrypted_symmetric_key_path)

        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )

        symmetric_key = AsymmetricEncryption.rsa_decrypt(private_key, encrypted_symmetric_key)

        encrypted_text = SymmetricalEncryption.encrypt_data(original_text, symmetric_key)
        write_binary_file(encrypt_text_path, encrypted_text)
    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе шифрования данных: {str(e)}")


def decrypt_data(encrypted_text_path: str,
                 private_key_path: str,
                 encrypted_symmetric_key_path: str,
                 decrypted_text_path: str) -> None:
    """
    Дешифрует данные
    :param encrypted_text_path: путь к файлц с зашифрованными данными
    :param private_key_path: путь к файлу с приватным RSA ключом
    :param encrypted_symmetric_key_path: путь к файлу с зашифрованным симметричным ключом
    :param decrypted_text_path: путь к файлу для сохранения расшифрованных данных
    :return:
    """
    try:
        encrypted_text = read_binary_file(encrypted_text_path)
        private_key_bytes = read_binary_file(private_key_path)
        encrypted_symmetric_key = read_binary_file(encrypted_symmetric_key_path)

        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )

        symmetric_key = AsymmetricEncryption.rsa_decrypt(private_key, encrypted_symmetric_key)

        decrypted_text = SymmetricalEncryption.decrypt_data(encrypted_text, symmetric_key)
        write_binary_file(decrypted_text_path, decrypted_text)
    except Exception as e:
        raise RuntimeError(f"Ошибка в процессе дешифрования данных: {str(e)}")


def update_key_size(key_size: int) -> None:
    """
    Изменяет размер ключа в settings.json
    :param key_size: новый размер ключа
    """
    try:
        if key_size not in [128, 192, 256]:
            raise ValueError("Размер ключа не подходит. Допустимые значения: 128, 192, 256")

        settings = read_json('settings.json')
        settings['key_size'] = key_size
        write_json('settings.json', settings)
        print(f"Размер ключа изменен на {key_size} бит")

    except Exception as e:
        raise RuntimeError(f"Ошибка при изменении размера ключа: {str(e)}")


def main() -> None:
    try:
        parser = argparse.ArgumentParser()

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-gen', '--generation', action='store_true', help='Режим генерации ключей')
        group.add_argument('-enc', '--encryption', action='store_true', help='Режим шифрования')
        group.add_argument('-dec', '--decryption', action='store_true', help='Режим дешифрования')
        group.add_argument('-key','--key-size', type=int, help='Изменить размер ключа')

        args = parser.parse_args()

        settings = read_json('settings.json')

        match (args.generation, args.encryption, args.decryption, args.key_size):
            case (True, False, False, None):
                print(f"Запуск генерации ключей ({settings['key_size']} бит)...")
                generate_keys(
                    settings['key_size'],
                    settings['public_key'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key']
                )
                print("Генерация ключей завершена успешно!")

            case (False, True, False, None):
                print("Запуск шифрования данных...")
                encrypt_data(
                    settings['original_text'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key'],
                    settings['encrypted_text']
                )
                print("Шифрование завершено успешно!")

            case (False, False, True, None):
                print("Запуск дешифрования данных...")
                decrypt_data(
                    settings['encrypted_text'],
                    settings['private_key'],
                    settings['encrypted_symmetric_key'],
                    settings['decrypted_text']
                )
                print("Дешифрование завершено успешно!")

            case (False, False, False, size):
                update_key_size(size)
            case _:
                raise ValueError("Неверная комбинация режимов работы")

    except Exception as e:
        print(f"Ошибка: {str(e)}")

if __name__ == '__main__':
    main()