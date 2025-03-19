import argparse

from argparse import Namespace
import sys

from  cipher import *


def parser_create() -> Namespace:
    """
    Parser

    :return: Parsed arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('input_text', type=str, help='Name of input text file')
    parser.add_argument('output_text', type=str, help='Name of output text file')
    parser.add_argument('key_filename', type=str, help='Filename containing the key')

    return parser.parse_args()
