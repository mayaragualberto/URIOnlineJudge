
//Receber dois números e imprimir a soma
import java.util.Scanner;

public class URI1003 {
    public static void main(String[] args) {
        int A, B, soma;
        Scanner input = new Scanner(System.in);
        A = input.nextInt();
        B = input.nextInt();
        soma = A + B;
        System.out.printf("SOMA = %s\n", soma);
    }
}
