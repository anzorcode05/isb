import math


from const import *


def read_file(filename: str) -> str:
    """
    Reads sequence

    :param filename: Path to the file to read.
    :return:  sequence
    """

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except Exception as e:

        print(f"Error reading file: {e}")

        def write_file(filename: str, text: str) -> None:
            """
            Writes and add text to a file.

            :param filename: Path to the file to write to.
            :param text: The text
            :return: None
            """

            try:

                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(text)

            except Exception as e:

                print(f"Error writing file: {e}")


