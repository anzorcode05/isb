#include <iostream>
#include <random>
#include <bitset>
#include <fstream>

void generate_bit_sequence() {
  std::random_device rd;
  std::mt19937_64 gen(rd());
  std::uniform_int_distribution<int> dist(0, 1);

  std::bitset<128> bits;
  for (int i = 0; i < 128; ++i) {
    bits[i] = dist(gen);
  }

  std::ofstream output_file("sequence_cpp.txt");
  output_file << bits;
  output_file.close();
}

int main() {
  generate_bit_sequence();
  return 0;
}