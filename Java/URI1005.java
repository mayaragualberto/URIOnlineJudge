
//Receber duas notas com um casa decimal e imprimir a média, considerando:
// nota A com peso 3.5 e nota B com peso 7.5
import java.util.Scanner;

public class URI1005 {
    public static void main(String[] args) {
        double A, B, media;
        Scanner input = new Scanner(System.in);
        A = input.nextDouble();
        B = input.nextDouble();
        media = ((A * 3.5) + (B * 7.5)) / 11;
        System.out.printf("MEDIA = %.5f\n", media);
    }
}
