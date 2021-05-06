
//Recebe o raio e calcula a área do círculo
import java.util.Scanner;

public class URI1002 {
    public static void main(String[] args) {
        double area, raio;
        Scanner input = new Scanner(System.in);
        raio = input.nextDouble();
        area = 3.14159 * (raio * raio);
        System.out.printf("A=%.4f\n", area);
    }
}
