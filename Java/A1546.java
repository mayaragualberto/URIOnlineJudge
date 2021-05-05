import java.util.Scanner;

public class A1546 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int m = entrada.nextInt();

        for (int i = 0; i < m; i++) {
            int k = entrada.nextInt();
            for (int j = 0; j < k; j++) {
                int feedback = entrada.nextInt();
                switch (feedback) {
                case 1:
                    System.out.println("Rolien");
                    break;
                case 2:
                    System.out.println("Naej");
                    break;
                case 3:
                    System.out.println("Elehcim");
                    break;
                case 4:
                    System.out.println("Odranoel");
                    break;
                }
            }
        }

    }
}