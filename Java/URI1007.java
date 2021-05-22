
//Calcular diferença de quatro valores seguindo a fórmula DIFERENCA = (A * B - C * D).
import java.util.Scanner;

public class URI1007 {
    public static void main(String[] args) {
        int A, B, C, D, DIFERENCA;
        Scanner input = new Scanner(System.in);
        A = input.nextInt();
        B = input.nextInt();
        C = input.nextInt();
        D = input.nextInt();
        DIFERENCA = (A * B - C * D);
        System.out.printf("DIFERENCA = %s\n", DIFERENCA);
    }
}