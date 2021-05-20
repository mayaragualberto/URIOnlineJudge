
//Receber dois números inteiros e imprimir o produto
import java.util.Scanner;

public class URI1004 {
    public static void main(String[] args) {
        int A, B, produto;
        Scanner input = new Scanner(System.in);
        A = input.nextInt();
        B = input.nextInt();
        produto = A * B;
        System.out.printf("PROD = %s\n", produto);
    }
}
