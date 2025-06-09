from tests import frequency_bit_test, identical_consecutive_bits_test, longest_sequence_of_ones_test
from work_with_files import read_file, read_json, write_json


def main():
    try:
        constants = read_json('consts.json')

        sequence_cpp = read_file(constants['sequence_cpp'])
        sequence_java = read_file(constants['sequence_java'])

        stats = {
            "C++ frequency bit test": frequency_bit_test(sequence_cpp),
            "Java frequency bit test": frequency_bit_test(sequence_java),
            "C++ identical bit sequence": identical_consecutive_bits_test(sequence_cpp),
            "Java identical bit sequence": identical_consecutive_bits_test(sequence_java),
            "C++ longest run of ones": longest_sequence_of_ones_test(sequence_cpp,constants['pi'],constants['m']),
            "Java longest run of ones": longest_sequence_of_ones_test(sequence_java,constants['pi'],constants['m'])
        }

        write_json(constants['result'], stats)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()