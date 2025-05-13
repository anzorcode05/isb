import math

from scipy.special import gammainc

from const import *


def read_file(filename: str) -> str:
    """
    Reads the sequence

    :param filename: Path to the file to read.
    :return: The sequence
    """

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except Exception as e:

        print(f"Error reading file: {e}")


def write_file(filename: str, text: str) -> None:
    """
    Writes the given text to a file.

    :param filename: Path to the file to write to.
    :param text: The text
    :return: None
    """

    try:

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:

        print(f"Error writing file: {e}")

def bit_frequency_analysis(bit_stream: str) -> float:
    """
    Analyzes the frequency of bits in a binary string.

    :param bit_stream: The binary sequence
    :return: Computed p-value
    """

    stream_length = len(bit_stream)

    if stream_length == 0:
        raise ValueError("Empty bit stream provided")

    sum_bits = sum([1 if b == "1" else -1 for b in bit_stream])

    p_val = math.erfc((abs(sum_bits) / math.sqrt(stream_length)) / math.sqrt(2))

    return p_val


def consecutive_bits_test(bit_sequence: str) -> float:
    """
    Checks for randomness by analyzing consecutive bit patterns.

    :param bit_sequence: The binary sequence
    :return: Computed p-value
    """

    p_val = 0.0

    seq_len = len(bit_sequence)

    prob_one = bit_sequence.count('1') / seq_len

    if abs(prob_one - 0.5) >= 2 / math.sqrt(seq_len):
        return p_val

    transitions = 0

    for i in range(seq_len - 1):
        if bit_sequence[i] != bit_sequence[i + 1]:
            transitions += 1

    num = abs(transitions - 2 * seq_len * prob_one * (1 - prob_one))
    denom = 2 * math.sqrt(2 * seq_len) * prob_one * (1 - prob_one)

    return math.erfc(num / denom)


def max_ones_block_test(data: str) -> float:
    """
    Evaluates the longest run of ones within fixed-length blocks.

    :param data: The binary sequence
    :return: Computed p-value
    """

    data_len = len(data)

    if data_len < 128:
        raise ValueError("Requires at least 128 bits")

    blocks_count = data_len // 8

    freq_counts = [0, 0, 0, 0]

    for block_idx in range(blocks_count):

        current_block = data[block_idx * 8 : (block_idx + 1) * 8]

        max_run_len = 0
        current_run = 0

        for bit in current_block:

            if bit == '1':
                current_run += 1
                max_run_len = max(max_run_len, current_run)
            else:
                current_run = 0

        match max_run_len:
            case 0 | 1:
                freq_counts[0] += 1
            case 2:
                freq_counts[1] += 1
            case 3:
                freq_counts[2] += 1
            case _:
                freq_counts[3] += 1

    chi_sq = 0.0

    for i in range(len(freq_counts)):
        chi_sq += (freq_counts[i] - 16 * PI[i]) ** 2 / (16 * PI[i])

    p_val = gammainc(3 / 2, chi_sq / 2)

    return p_val


def main():

    cpp_bits = read_file(cpp_sequence_txt)
    java_bits = read_file(java_sequence_txt)

    cpp_freq_p = bit_frequency_analysis(cpp_bits)
    cpp_runs_p = consecutive_bits_test(cpp_bits)
    cpp_block_p = max_ones_block_test(cpp_bits)

    cpp_report = (f"CPP bit stream: {cpp_bits}\n\n"
                 f"Bit frequency analysis: {cpp_freq_p}\n"
                 f"Consecutive bits randomness test: {cpp_runs_p}\n"
                 f"Max ones block evaluation: {cpp_block_p}")

    write_file(res_test_cpp, cpp_report)

    java_freq_p = bit_frequency_analysis(java_bits)
    java_runs_p = consecutive_bits_test(java_bits)
    java_block_p = max_ones_block_test(java_bits)

    java_report = (f"Java bit stream: {java_bits}\n\n"
                  f"Bit frequency analysis: {java_freq_p}\n"
                  f"Consecutive bits randomness test: {java_runs_p}\n"
                  f"Max ones block evaluation: {java_block_p}")

    write_file(res_test_java, java_report)


if __name__ == "__main__":
    main()

