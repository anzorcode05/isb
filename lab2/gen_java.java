import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        StringBuilder bits = new StringBuilder(128);
        for (int i = 0; i < 128; i++) {
            bits.append((int) (Math.random() * 2));
        }
        String sequence = bits.toString();
        System.out.println(sequence);
    }
}