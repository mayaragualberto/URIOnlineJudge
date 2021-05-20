
//Receber três notas com um casa decimal e imprimir a média, considerando:
// nota A com peso 2, nota B com peso 3 e nota C com peso 5
import java.util.Scanner;

public class URI1006 {
    public static void main(String[] args) {
        double A, B, C, media;
        Scanner input = new Scanner(System.in);
        A = input.nextDouble();
        B = input.nextDouble();
        C = input.nextDouble();
        media = ((A * 2) + (B * 3) + (C * 5)) / 10;
        System.out.printf("MEDIA = %.1f\n", media);
    }
}
