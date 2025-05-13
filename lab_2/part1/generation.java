import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class getRandomSequence {
    public static final int BIT_LENGTH = 128;

    public static void main(String[] args) {
        StringBuilder sequence = new StringBuilder();
        Random random = new Random();

        for (int i = 0; i < BIT_LENGTH; i++) {
            int bit = random.nextInt(2);
            sequence.append(bit);
        }

        try (FileWriter writer = new FileWriter("sequenceJAVA.txt")) {
            writer.write(sequence.toString());
            System.out.println("Sequence saved to sequenceJAVA.txt");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }
}