
//Informar a quantidade de LEDs de acordo com o número a ser mostrado
import java.util.Scanner;

public class URI1168 {
    public static int calculaTotal(String n) {
        int total = 0;

        for (int i = 0; i < n.length(); i++) {
            switch (n.charAt(i)) {
                case '0':
                case '6':
                case '9':
                    total += 6;
                    break;
                case '2':
                case '3':
                case '5':
                    total += 5;
                    break;
                case '1':
                    total += 2;
                    break;
                case '4':
                    total += 4;
                    break;
                case '7':
                    total += 3;
                    break;
                case '8':
                    total += 7;
                    break;

            }
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int testes, tracos;
        String numero;

        testes = input.nextInt();

        for (int i = 0; i < testes; i++) {
            numero = input.next();
            tracos = calculaTotal(numero);

            System.out.println(tracos + " leds");
        }
    }
}
