
//Construir matriz de acordo com a ordem lida;
//Encerrar com entrada 0
import java.util.Scanner;

public class URI1435 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        while (n != 0) {
            for (int linha = 0; linha < n; linha++) {
                for (int coluna = 0; coluna < n; coluna++) {
                    if (linha + coluna < n) {
                        System.out.printf("%3d", min(linha + 1, coluna + 1));
                    } else {
                        System.out.printf("%3d", min(n - linha, n - coluna));
                    }
                    if (coluna < n - 1) {
                        System.out.print(" ");
                    }
                }
                System.out.println("");
            }
            n = input.nextInt();
            System.out.println("");
        }
    }

    public static int min(int a, int b) {
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }
}
