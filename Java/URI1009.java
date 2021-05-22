
//Retornar salário com bônus
import java.util.Scanner;

public class URI1009 {
    public static void main(String[] args) {
        String nome;
        double salarioFixo, totalVendas, salarioBonus;
        Scanner input = new Scanner(System.in);
        nome = input.next();
        salarioFixo = input.nextDouble();
        totalVendas = input.nextDouble();
        salarioBonus = (salarioFixo + (totalVendas * 0.15));
        System.out.printf("TOTAL = R$ %.2f\n", salarioBonus);
    }
}