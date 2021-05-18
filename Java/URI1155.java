//Calcular S, sendo S = 1 + 1/2 + 1/3 + … + 1/100
public class URI1155 {
    public static void main(String[] args) {
        System.out.printf("%.2f\n", sequenciaRecursiva(1));
    }

    public static float sequenciaRecursiva(float n) {
        if (n < 100) {
            return 1 / n + sequenciaRecursiva(n + 1);
        } else {
            return 1 / n;
        }
    }
}
