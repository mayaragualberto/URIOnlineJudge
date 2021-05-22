
//Retornar salário com bônus
import java.util.Scanner;

public class URI1010 {
    public static void main(String[] args) {
        int codigoA, codigoB, qtdA, qtdB;
        double valorA, valorB, valorTotal;
        Scanner input = new Scanner(System.in);
        codigoA = input.nextInt();
        qtdA = input.nextInt();
        valorA = input.nextDouble();
        codigoB = input.nextInt();
        qtdB = input.nextInt();
        valorB = input.nextDouble();
        valorTotal = (qtdA * valorA) + (qtdB * valorB);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", valorTotal);
    }
}