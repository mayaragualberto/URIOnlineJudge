
//Recebe o número do funcionário, horas trabalhadas e valor por hora. Imprime o salário
import java.util.Scanner;

public class URI1008 {
    public static void main(String[] args) {
        int A, B;
        double C, salario;
        Scanner input = new Scanner(System.in);
        A = input.nextInt();
        B = input.nextInt();
        C = input.nextDouble();
        salario = (B * C);
        System.out.printf("NUMBER = %s\n", A);
        System.out.printf("SALARY = U$ %.2f\n", salario);
    }
}