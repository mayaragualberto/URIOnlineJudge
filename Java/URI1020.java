
//Lê uma idade em dias e converte em ano, meses e dias.
import java.util.Scanner;

public class URI1020 {
    public static void main(String[] args) {
        int idade, anos, meses, dias, resto;
        Scanner input = new Scanner(System.in);
        idade = input.nextInt();
        anos = idade / 365;
        resto = idade % 365;
        meses = resto / 30;
        resto = resto % 30;
        dias = resto;
        System.out.println(anos + " ano(s)\n" + meses + " mes(es)\n" + dias + " dia(s)");
    }
}
